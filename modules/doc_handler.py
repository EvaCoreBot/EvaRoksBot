from io import BytesIO
from typing import Optional

from telegram import Update
from telegram.ext import ContextTypes
from docx import Document


def _extract_text(data: bytes, ext: str) -> str:
    """Return extracted text depending on extension."""
    ext = ext.lower()
    if ext == "pdf":
        import fitz  # PyMuPDF
        doc = fitz.open(stream=data, filetype="pdf")
        text = "".join(page.get_text() for page in doc)
        return text
    if ext in {"doc", "docx"}:
        doc = Document(BytesIO(data))
        return "\n".join(p.text for p in doc.paragraphs)
    if ext in {"png", "jpg", "jpeg"}:
        from PIL import Image
        import pytesseract
        image = Image.open(BytesIO(data))
        return pytesseract.image_to_string(image, lang="rus+eng")
    return ""


async def handle_doc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle an uploaded document or prompt for one."""
    document = update.message.document
    photo = update.message.photo[-1] if update.message.photo else None
    if not document and not photo:
        await update.message.reply_text("📄 Отправьте PDF, DOCX или изображение")
        return

    tg_file = await (document.get_file() if document else photo.get_file())
    data = await tg_file.download_as_bytearray()
    filename = document.file_name if document else f"photo.{tg_file.file_path.split('.')[-1]}"
    ext = filename.split(".")[-1]
    text = _extract_text(bytes(data), ext)

    history = context.application.bot_data.setdefault("history", [])
    history.append(filename)
    snippet = text[:200].replace("\n", " ") if text else "(не удалось извлечь текст)"
    await update.message.reply_text(f"📑 {filename}: {snippet}")
