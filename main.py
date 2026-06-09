import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# BOT TOKEN GitHub Secret se aayega
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🛍️ View Products",
                url="https://foreverliving.com",
            )
        ],
        [
            InlineKeyboardButton(
                "💼 Join Business",
                url="https://forms.gle/X75rdngzoQDnmUeq5",
            )
        ],
        [
            InlineKeyboardButton(
                "📞 WhatsApp",
                url="https://wa.me/917984200815",
            )
        ],
        [
            InlineKeyboardButton(
                "📸 Instagram",
                url="https://instagram.com/foreverby_nik",
            )
        ],
        [
            InlineKeyboardButton(
                "💬 Telegram",
                url="https://t.me/ForeverNIK2",
            )
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🌿 Welcome to Forever Living Products By Nik 💚\n\n"
        "Choose an option below:",
        reply_markup=reply_markup,
    )


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable not found!")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot Started Successfully...")

    app.run_polling()


if __name__ == "__main__":
    main()
