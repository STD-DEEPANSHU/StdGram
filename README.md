# StdGram

[![PyPI version](https://img.shields.io/pypi/v/stdgram.svg?color=blue)](https://pypi.org/project/stdgram/)
[![Python versions](https://img.shields.io/pypi/pyversions/stdgram.svg)](https://pypi.org/project/stdgram/)
[![License](https://img.shields.io/badge/license-LGPLv3%20%2F%20GPLv3-blue.svg)](LICENSE)
[![CI](https://github.com/STD-DEEPANSHU/StdGram/actions/workflows/ci.yml/badge.svg)](https://github.com/STD-DEEPANSHU/StdGram/actions)

**StdGram** is a modern, asynchronous Telegram MTProto client and framework for Python.

Built as an actively maintained, drop-in alternative to Pyrogram, StdGram addresses long-standing developer pain points around rate-limiting, missing MTProto features, and conversation state management. It allows developers to build bots, userbots, and custom Telegram tools with clean, readable async/await syntax.

---

## Highlights

- **Drop-in Pyrogram Compatibility:** Switch existing codebases by simply updating imports. Handlers, filters, and methods remain fully compatible.
- **Automatic FloodWait Handling:** No more wrapping calls in repetitive `try...except FloodWait` blocks. StdGram queues throttled calls and retries them automatically.
- **Native Conversations (`client.ask`):** Ask interactive questions and wait for user replies in a single line of code, without third-party monkey patches.
- **Modern Telegram Layer Support:** Full MTProto support for recent Telegram additions, including **Stories**, **Gifts**, **Forum Topics**, and **Business Accounts**.
- **Fast Cryptography:** High-performance encryption powered by `TgCrypto` C-extensions, with automatic pure-Python fallback.

---

## Installation

Install the stable release from PyPI:

```bash
pip install stdgram
```

For optional dependencies (fast crypto, cloud database sessions, async file utilities):

```bash
pip install stdgram[all]
```

---

## Quickstart

### 1. Basic Bot

```python
from stdgram import Client, filters

app = Client(
    "my_bot",
    api_id=12345,
    api_hash="0123456789abcdef0123456789abcdef",
    bot_token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text(f"Hello {message.from_user.first_name}! Powered by StdGram.")

@app.on_message(filters.text & filters.private)
async def echo_handler(client, message):
    # Automatically rate-limit safe
    await message.reply_text(message.text)

if __name__ == "__main__":
    app.run()
```

---

### 2. Interactive Conversations (`client.ask`)

Gather user input sequentially without complicated state machines:

```python
from stdgram import Client, filters
from stdgram.errors import ConversationTimeout

app = Client("conversation_bot", bot_token="YOUR_BOT_TOKEN")

@app.on_message(filters.command("register"))
async def register(client, message):
    chat_id = message.chat.id

    try:
        name_msg = await client.ask(chat_id, "What is your name?", timeout=60)
        age_msg = await client.ask(chat_id, "How old are you?", timeout=60)

        await message.reply_text(
            f"Registration complete!\n"
            f"Name: {name_msg.text}\n"
            f"Age: {age_msg.text}"
        )
    except ConversationTimeout:
        await message.reply_text("Session timed out. Please run /register again.")

app.run()
```

---

### 3. Migrating from Pyrogram

If you have an existing Pyrogram project, migrate in two steps:

1. Update your dependencies:
   ```bash
   pip uninstall pyrogram
   pip install stdgram
   ```

2. Replace the import statement:
   ```python
   # Old
   from pyrogram import Client, filters

   # New
   from stdgram import Client, filters
   ```

All existing handler definitions, filters, sessions, and methods work as expected.

---

## Examples

Check the [`examples/`](examples/) directory for working starter templates:

- [`01_simple_bot.py`](examples/01_simple_bot.py) — Standard bot commands and echo logic.
- [`02_conversation_bot.py`](examples/02_conversation_bot.py) — Multi-step registration conversation flow.
- [`03_userbot.py`](examples/03_userbot.py) — User account automation with `.ping` and self-commands.

---

## License & Acknowledgements

StdGram is free and open-source software licensed under the **GNU Lesser General Public License v3.0 (LGPL-3.0)** with **GNU GPLv3** terms. See the [LICENSE](LICENSE) and [COPYING.lesser](COPYING.lesser) files for complete details.

StdGram is maintained by **[STD-DEEPANSHU](https://github.com/STD-DEEPANSHU)** and contributors. It builds upon foundational engineering from the open-source Telegram community, notably:

- **[Dan](https://github.com/delivrance)** for creating the original [Pyrogram](https://github.com/pyrogram/pyrogram).
- **[Kurigram](https://github.com/kurigram-org/kurigram)** for upstream layer tracking.
- **[Lonami](https://github.com/LonamiWebs)** for pioneering Python MTProto research via [Telethon](https://github.com/LonamiWebs/Telethon).
