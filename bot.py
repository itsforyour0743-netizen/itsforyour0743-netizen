# My Telegram Bot

Ye ek simple Telegram bot hai jo /start command pe message reply karta hai.

```python
# bot.py - Simple Telegram Bot Starter

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Main aapka bot hoon 😎")

if __name__ == "__main__":
    if not TOKEN:
        print("Error: Telegram token set nahi hai!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.run_polling()
```
