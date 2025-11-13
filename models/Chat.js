const mongoose = require('mongoose');

const ChatSchema = new mongoose.Schema({
  chatType: { type: String, enum: ['dm', 'group'], default: 'dm' },
  members: [mongoose.Schema.Types.ObjectId],
  name: String,
  lastMessageAt: Date,
});

module.exports = mongoose.model('Chat', ChatSchema);
