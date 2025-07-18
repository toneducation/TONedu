import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    update.message.reply_text("👋 Welcome to TONedu! Send /ask <topic> to learn something.")

def ask(update, context):
    topic = ' '.join(context.args)
    if topic:
        update.message.reply_text(f"📚 AI explanation for '{topic}':\n(This is a placeholder)")
    else:
        update.message.reply_text("❗Please provide a topic. Example: /ask Photosynthesis")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ask", ask))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
