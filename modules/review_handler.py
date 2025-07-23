from telegram import Update
from telegram.ext import ContextTypes

async def handle_review(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Return a placeholder contract review."""
    await update.message.reply_text(
        "📝 Анализ договора: пункт 4.2 требует уточнения сроков."
    )
