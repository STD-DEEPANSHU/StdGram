<div align="center">

# ⚡ StdGram
### The Next-Generation, Production-Ready MTProto Framework for Python

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](https://www.python.org/)
[![Telegram MTProto](https://img.shields.io/badge/MTProto-2.0-blueviolet)](https://core.telegram.org/mtproto)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/STD-DEEPANSHU/StdGram)

<p align="center">
  <b>StdGram</b> is an ultra-fast, modern, asynchronous Telegram MTProto API client and bot framework for Python.
  <br />
  Engineered with native <b>Auto-FloodWait handling</b>, <b>Turbo Media transfer</b>, and built-in <b>Conversation states</b>.
</p>

[Key Features](#-key-features) •
[Installation](#-installation) •
[Quick Start](#-quick-start) •
[License & Attribution](#-license--legal-attribution) •
[Authors](#-authors)

---

</div>

## 🚀 Why StdGram?

While traditional MTProto libraries require extensive boilerplate and crash on rate limits, **StdGram** is engineered as a "batteries-included" framework designed for production stability:

- 🛡️ **Native Auto-FloodWait Queue:** No more messy `try...except FloodWait` blocks. StdGram automatically catches, queues, and safely dispatches messages without crashing.
- ⚡ **Turbo Parallel Media Engine:** Up to 3x faster upload and download speeds for large files (up to 4 GB) through concurrent MTProto chunks.
- 💬 **Native Conversations (`client.ask`):** Intuitive multi-step input flows and finite state handling directly in the core client.
- ☁️ **Cloud-Native Storage:** Direct support for MongoDB, PostgreSQL, and Redis session strings—eliminating missing local `.session` file issues on Heroku, Docker, and Render.
- 🧩 **Modular Architecture:** Use minimal core MTProto or opt-in to advanced toolkits via `pip install stdgram[all]`.
- 🔒 **Strong Copyleft Protection:** Protected under **GNU GPLv3** with strict author attribution clauses to prevent closed-source proprietary forks.

---

## 📦 Installation

```bash
# Standard Core Client
pip install stdgram

# Production Suite (Fast Crypto, Redis, Storage)
pip install stdgram[all]
```

---

## ⚡ Quick Start

### 1. Simple Bot Example
```python
from stdgram import Client, filters

app = Client(
    "my_bot",
    api_id=12345,
    api_hash="YOUR_API_HASH",
    bot_token="YOUR_BOT_TOKEN"
)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text(
        "👋 Welcome! Powered by **StdGram** — The Next-Gen Telegram Engine."
    )

app.run()
```

### 2. Interactive Conversation Example (`client.ask`)
```python
@app.on_message(filters.command("register"))
async def register_user(client, message):
    chat_id = message.chat.id
    
    # Simple 1-line interactive prompt
    name_response = await client.ask(chat_id, "What is your name?")
    user_name = name_response.text
    
    await message.reply_text(f"Welcome aboard, {user_name}!")
```

---

## 📜 License & Legal Attribution

StdGram is free software released under the **GNU General Public License v3.0 (GPLv3)** with **Section 7 Additional Terms**.

### ⚠️ Strict Terms for Forks and Derivative Works:
1. **Never Closed-Source:** Any project derived from StdGram **MUST** remain 100% free and open-source under GNU GPLv3. You may NOT privatize or sell proprietary closed forks of this software.
2. **Prominent Credit Required:** Any redistribution or modified version must explicitly retain the name **StdGram**, link to the original repository, and acknowledge **STD-DEEPANSHU** in the main README and startup console notices.
3. For full terms, see the [LICENSE](LICENSE) and [NOTICE](NOTICE) files.

---

## 👥 Authors

- **Deepanshu (STD-DEEPANSHU)** — Lead Architect & Creator ([@STD-DEEPANSHU](https://github.com/STD-DEEPANSHU))
- Upstream acknowledgements: [Dan (Pyrogram)](https://github.com/pyrogram/pyrogram), [Kurigram](https://github.com/kurigram-org/kurigram), [Telethon](https://github.com/LonamiWebs/Telethon), and the open-source community. See [AUTHORS.md](AUTHORS.md).
