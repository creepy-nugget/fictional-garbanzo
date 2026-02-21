import os
import logging
import psutil
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder ,ContextTypes,CommandHandler

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Hello ,I am a bot made by Sankalp"
    ) 

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    await update.message.reply_text(f"🖥 **Server Status:**\nCPU: {cpu}%\nRAM: {ram}%")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    status_handler = CommandHandler('status',status)
    application.add_handler(start_handler)
    application.add_handler(status_handler)

    print("Bot is checking for messages...")
    application.run_polling()
