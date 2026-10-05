# StdGram Official Examples

This directory provides clean, production-ready starter templates for building bots and userbots using **StdGram**:

| Example | Description |
| :--- | :--- |
| [`01_simple_bot.py`](01_simple_bot.py) | A simple Telegram Bot with command handler and auto-floodwait protected text replies. |
| [`02_conversation_bot.py`](02_conversation_bot.py) | Demonstrates native `client.ask(...)` multi-step interactive conversations without external plugins. |
| [`03_userbot.py`](03_userbot.py) | Telegram User Account automation (MTProto userbot) with prefix commands. |

### How to Run:
1. Install StdGram:
   ```bash
   pip install stdgram
   ```
2. Replace `api_id`, `api_hash`, and `bot_token` with your credentials.
3. Run the script:
   ```bash
   python 01_simple_bot.py
   ```
