"""
StdGram Example 2: Interactive Conversation & Multi-Step Prompts
Demonstrates the native `client.ask(...)` engine without external plugins.
"""

from stdgram import Client, filters
from stdgram.errors import ConversationTimeout

app = Client(
    "conversation_bot",
    api_id=12345,
    api_hash="YOUR_API_HASH",
    bot_token="YOUR_BOT_TOKEN"
)

@app.on_message(filters.command("register"))
async def register_flow(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    try:
        # Step 1: Ask for name
        name_reply = await client.ask(
            chat_id=chat_id,
            text="👋 Welcome to registration! What is your full name?",
            user_id=user_id,
            timeout=60
        )
        full_name = name_reply.text

        # Step 2: Ask for email
        email_reply = await client.ask(
            chat_id=chat_id,
            text=f"Nice to meet you, {full_name}! What is your email address?",
            user_id=user_id,
            timeout=60
        )
        email = email_reply.text

        # Step 3: Confirmation
        await message.reply_text(
            f"✅ **Registration Complete!**\n\n"
            f"• **Name:** {full_name}\n"
            f"• **Email:** {email}\n\n"
            f"Powered natively by StdGram `client.ask()`!"
        )

    except ConversationTimeout:
        await message.reply_text("⏳ Registration timed out. Send /register to try again.")

if __name__ == "__main__":
    print("Starting Conversation Bot...")
    app.run()
