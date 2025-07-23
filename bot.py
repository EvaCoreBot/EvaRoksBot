import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler
from modules.doc_handler import handle_doc
from modules.risk_handler import handle_risk
from modules.review_handler import handle_review
from modules.prompt_handler import handle_prompt
from modules.generate_handler import handle_generate
from modules.history_handler import handle_history

load_dotenv()

async def start(update, context):
    await update.message.reply_text(
        "Eva.Юрист подключена. Команды: /doc /generate /history /risk /review /prompt"
    )


def get_app():
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN is not set")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("doc", handle_doc))
    app.add_handler(CommandHandler("generate", handle_generate))
    app.add_handler(CommandHandler("history", handle_history))
    app.add_handler(CommandHandler("risk", handle_risk))
    app.add_handler(CommandHandler("review", handle_review))
    app.add_handler(CommandHandler("prompt", handle_prompt))
    return app


def handler(request):
    get_app()  # Build the app so that webhook routes are registered.
    return {"statusCode": 200, "body": "Telegram webhook active"}


if __name__ == "__main__":
    application = get_app()
    application.run_polling()
