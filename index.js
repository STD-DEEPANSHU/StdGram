const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const cors = require('cors');
require('dotenv').config();

const User = require('./models/User');
const Chat = require('./models/Chat');
const Message = require('./models/Message');

const app = express();
app.use(cors({ origin: '*' }));
app.use(bodyParser.json());

// --- MongoDB Connection ---
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('✅ MongoDB connected'))
.catch((err) => console.error('❌ MongoDB connection error:', err));

const JWT_SECRET = process.env.JWT_SECRET || 'devsecret';

// --- Root route ---
app.get('/', (req, res) => {
  res.send('Backend running ✅ MongoDB connected');
});

// --- Auth Routes ---
app.post('/api/register', async (req, res) => {
  try {
    const { username, name, password } = req.body;
    if (!username || !password) return res.status(400).json({ error: 'Missing fields' });

    const exists = await User.findOne({ username });
    if (exists) return res.status(400).json({ error: 'Username taken' });

    const user = new User({ username, name, passwordHash: password });
    await user.save();

    const token = jwt.sign({ id: user._id }, JWT_SECRET, { expiresIn: '7d' });
    res.json({ user, token });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Server error' });
  }
});

app.post('/api/login', async (req, res) => {
  try {
    const { username, password } = req.body;
    const user = await User.findOne({ username });
    if (!user || user.passwordHash !== password)
      return res.status(401).json({ error: 'Invalid credentials' });

    const token = jwt.sign({ id: user._id }, JWT_SECRET, { expiresIn: '7d' });
    res.json({ user, token });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Server error' });
  }
});

// --- Chat APIs ---
app.post('/api/chats', async (req, res) => {
  try {
    const chat = new Chat(req.body);
    await chat.save();
    res.json(chat);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Chat creation failed' });
  }
});

app.get('/api/chats/:chatId/messages', async (req, res) => {
  try {
    const msgs = await Message.find({ chatId: req.params.chatId }).sort({ createdAt: 1 });
    res.json(msgs);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to fetch messages' });
  }
});

// --- HTTP + Socket.IO ---
const server = http.createServer(app);
const io = new Server(server, {
  cors: { origin: '*', methods: ['GET', 'POST'] },
});

// --- Socket Auth ---
io.use((socket, next) => {
  try {
    const token = socket.handshake.auth.token;
    const user = jwt.verify(token, JWT_SECRET);
    socket.userId = user.id;
    next();
  } catch {
    next(new Error('Unauthorized'));
  }
});

// --- Socket Events ---
io.on('connection', (socket) => {
  console.log('⚡ User connected:', socket.userId);

  socket.on('join_chat', (chatId) => {
    socket.join(chatId);
    console.log(`📩 User ${socket.userId} joined chat ${chatId}`);
  });

  socket.on('send_message', async ({ chatId, text }) => {
    try {
      const msg = new Message({ chatId, sender: socket.userId, text });
      await msg.save();
      await Chat.findByIdAndUpdate(chatId, { lastMessageAt: new Date() });
      io.to(chatId).emit('message', msg);
    } catch (err) {
      console.error('Message send error:', err);
    }
  });

  socket.on('disconnect', (reason) => {
    console.log(`❌ User disconnected: ${socket.userId} (${reason})`);
  });
});

const PORT = process.env.PORT || 4000;
server.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));
