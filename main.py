import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    kb = [
        [InlineKeyboardButton("🌹 بوكيه أحمر 150ر", callback_data="red")],
        [InlineKeyboardButton("🤍 بوكيه أبيض 140ر", callback_data="white")],
        [InlineKeyboardButton("💐 بوكيه مشكل 200ر", callback_data="mix")],
        [InlineKeyboardButton("📞 تواصل", callback_data="contact")]
    ]
    await update.message.reply_text("أهلاً بك في وكيل الورد 🌹\nاختر:", reply_markup=InlineKeyboardMarkup(kb))

async def btn(update, context):
    q = update.callback_query
    await q.answer()
    if q.data == "contact":
        await q.message.reply_text("جدة - واتساب: 05XXXXXXXX")
    else:
        await q.message.reply_text(f"تم اختيار {q.data} 🌹 أرسل موقعك")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(btn))
    app.run_polling()

if __name__ == "__main__":
    main()
