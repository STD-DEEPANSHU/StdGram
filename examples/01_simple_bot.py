"""
StdGram Example 1: Simple Echo & Start Bot
Run with your Bot Token from @BotFather.
"""

from stdgram import Client, filters

app = Client(
    "echo_bot",
    api_id=12345,  # Replace with your API ID from my.telegram.org
    api_hash="YOUR_API_HASH",  # Replace with your API Hash
    bot_token="YOUR_BOT_TOKEN"  # Replace with your Bot Token
)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text(
        f"Hello {message.from_user.first_name}!\n"
        "I am running on **StdGram** — The Next-Gen Telegram MTProto Framework! ⚡"
    )

@app.on_message(filters.text & filters.private)
async def echo_handler(client, message):
    # Automatically protected against Telegram FloodWait
    await message.reply_text(f"You said: {message.text}")

if __name__ == "__main__":
    print("Starting Echo Bot...")
    app.run()
