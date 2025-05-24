from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os

TOKEN = os.environ.get("TOKEN")  # Render 환경변수에서 가져옴
CHANNEL_ID = "-1002604713189"  # HUTTCOIN channel ID

# Welcome message function
async def send_welcome_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        welcome_text = """🎉 Welcome!

This is the **HUTTCOIN Community**.
HUTTCOIN is a coin that values absurdity and fun.

💼 CA : 9QNWgfQnteoVN7Mjk3xq5PxdXDVhWxFo1XSniUcRpump

✅ Available commands:
- /start : View the welcome message 👋
- /chart : View HUTTCOIN price chart 📈
- /x : Check the latest HUTTCOIN info 🔍
- /homepage : Visit the official website 🌐

💬 Community rules:
1. Enjoy nonsense, but respect each other.
2. Freely share your ideas and have fun!

Try using /chart, /x, or /homepage to explore more! 🚀"""

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=welcome_text
        )
        print(f"✅ Welcome message sent!")
    except Exception as e:
        print(f"Error occurred: {e}")

# Command handlers
async def chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📈 HUTTCOIN Chart: https://pump.fun/coin/9QNWgfQnteoVN7Mjk3xq5PxdXDVhWxFo1XSniUcRpump")

async def x(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Latest HUTTCOIN Info: https://x.com/huttcoin")

async def homepage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌐 Official Website: https://www.huttcoin.com")

# Channel command handler
async def handle_channel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        text = update.channel_post.text
        print(f"✅ Channel command received: {text}")

        if text.startswith('/chart'):
            await update.channel_post.reply_text("📈 HUTTCOIN Chart: https://pump.fun/coin/9QNWgfQnteoVN7Mjk3xq5PxdXDVhWxFo1XSniUcRpump")
        elif text.startswith('/x'):
            await update.channel_post.reply_text("🔍 Latest HUTTCOIN Info: https://huttcoin.com/info")
        elif text.startswith('/homepage'):
            await update.channel_post.reply_text("🌐 Official Website: https://huttcoin.netlify.app")
        elif text == "/start":
            await send_welcome_message(update, context)
        else:
            await update.message.reply_text("❗ Unknown command.")
            
# Group command handler
async def handle_group_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(f"✅ Group command received: {text}")

    if text == "/chart":
        await update.message.reply_text("📈 HUTTCOIN Chart: https://huttcoin.com/chart")
    elif text == "/x":
        await update.message.reply_text("🔍 Latest HUTTCOIN Info: https://https://x.com/huttcoin")
    elif text == "/homepage":
        await update.message.reply_text("🌐 Official Website: https://huttcoin.com")
    elif text == "/start":
        await send_welcome_message(update, context)
    else:
        await update.message.reply_text("❗ Unknown command.")

# Main function to run the bot
def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", send_welcome_message))
    application.add_handler(CommandHandler("chart", chart))
    application.add_handler(CommandHandler("x", x))
    application.add_handler(CommandHandler("homepage", homepage))

    # Add message handlers for channel and group
    application.add_handler(MessageHandler(filters.ChatType.CHANNEL & filters.TEXT, handle_channel_command))
    application.add_handler(MessageHandler(filters.ChatType.GROUP & filters.TEXT, handle_group_command))

    # Start polling
    print("✅ HUTTCOIN bot is running...")
    application.run_polling()

# Start execution
if __name__ == "__main__":
    main()
