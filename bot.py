import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load token from .env file
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to TONedu! Send /ask <topic> to learn something.")

# /ask command
async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = ' '.join(context.args)
    if topic:
        await update.message.reply_text(f"📚 AI explanation for '{topic}':\n(This is a placeholder)")
    else:
        await update.message.reply_text("❗Please provide a topic. Example: /ask Photosynthesis")

# Main bot runner
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask))

    print("🤖 BOT IS RUNNING...")
    app.run_polling()

if __name__ == "__main__":
    main()
