import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# توکن شما که به صورت امن از تنظیمات سرور خوانده می‌شود
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    # پاسخ ربات (می‌توانید بعداً به هوش مصنوعی متصلش کنید)
    response_text = f"سلام! پیام شما دریافت شد: {user_message}"
    await update.message.reply_text(response_text)

def main():
    if not TOKEN:
        print("خطا: توکن ربات یافت نشد!")
        return
        
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("ربات ابری نوا روشن شد...")
    app.run_polling()

if __name__ == "__main__":
    main()