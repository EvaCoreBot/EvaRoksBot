from telegram import Update
from telegram.ext import ContextTypes

async def handle_history(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Display list of processed documents."""
    history = context.application.bot_data.get("history", [])
    if not history:
        await update.message.reply_text("История пуста.")
    else:
        lines = "\n".join(history)
        await update.message.reply_text(f"Последние документы:\n{lines}")
