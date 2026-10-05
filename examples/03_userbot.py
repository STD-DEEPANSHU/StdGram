"""
StdGram Example 3: Telegram Userbot / Account Automation
Runs with your own Telegram user account via phone login or session string.
"""

from stdgram import Client, filters

# Initialize Userbot
app = Client(
    "my_userbot",
    api_id=12345,  # From https://my.telegram.org
    api_hash="YOUR_API_HASH"
)

# Command triggered only by yourself (.ping)
@app.on_message(filters.me & filters.command("ping", prefixes="."))
async def ping_cmd(client, message):
    await message.edit_text("🏓 **Pong!** Running smooth on **StdGram** ⚡")

# Auto-reaction or custom userbot automation
@app.on_message(filters.me & filters.command("alive", prefixes="."))
async def alive_cmd(client, message):
    me = await client.get_me()
    await message.edit_text(
        f"🤖 **StdGram Userbot Active**\n"
        f"• **User:** {me.first_name} (@{me.username})\n"
        f"• **Engine:** StdGram MTProto Framework\n"
        f"• **Protection:** Native Auto-FloodWait Enabled"
    )

if __name__ == "__main__":
    print("Starting Userbot...")
    app.run()
