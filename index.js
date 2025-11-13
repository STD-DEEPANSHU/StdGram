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
app.use(cors());
app.use(bodyParser.json());

// Connect MongoDB
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('✅ MongoDB connected'))
  .catch(err => console.error(err));

const JWT_SECRET = process.env.JWT_SECRET || 'devsecret';

// --- Auth ---
app.post('/api/register', async (req, res) => {
  const { username, name, password } = req.body;
  const exists = await User.findOne({ username });
  if (exists) return res.status(400).json({ error: 'Username taken' });
  const user = new User({ username, name, passwordHash: password });
  await user.save();
  const token = jwt.sign({ id: user._id }, JWT_SECRET);
  res.json({ user, token });
});

app.post('/api/login', async (req, res) => {
  const { username, password } = req.body;
  const user = await User.findOne({ username });
  if (!user || user.passwordHash !== password) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  const token = jwt.sign({ id: user._id }, JWT_SECRET);
  res.json({ user, token });
});

// --- Chat APIs ---
app.post('/api/chats', async (req, res) => {
  const chat = new Chat(req.body);
  await chat.save();
  res.json(chat);
});

app.get('/api/chats/:chatId/messages', async (req, res) => {
  const msgs = await Message.find({ chatId: req.params.chatId }).sort({ createdAt: 1 });
  res.json(msgs);
});

// --- HTTP + Socket.IO ---
const server = http.createServer(app);
const io = new Server(server, { cors: { origin: '*' } });

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

io.on('connection', (socket) => {
  console.log('⚡ user connected:', socket.userId);

  socket.on('join_chat', (chatId) => socket.join(chatId));

  socket.on('send_message', async ({ chatId, text }) => {
    const msg = new Message({ chatId, sender: socket.userId, text });
    await msg.save();
    await Chat.findByIdAndUpdate(chatId, { lastMessageAt: new Date() });
    io.to(chatId).emit('message', msg);
  });

  socket.on('disconnect', () => console.log('❌ user disconnected', socket.userId));
});

const PORT = process.env.PORT || 4000;
server.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));
