const mongoose = require('mongoose');

const MessageSchema = new mongoose.Schema({
  chatId: mongoose.Schema.Types.ObjectId,
  sender: mongoose.Schema.Types.ObjectId,
  text: String,
  attachments: Array,
  createdAt: { type: Date, default: Date.now },
});

module.exports = mongoose.model('Message', MessageSchema);
