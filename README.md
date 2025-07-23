# EvaRoksBot

Prototype Telegram bot for basic legal document handling. It uses
`python-telegram-bot` and includes handlers for generating documents,
extracting text from uploads and showing history.

## Quick start

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file and place your credentials there:

```
TELEGRAM_TOKEN=your_token
GEMINI_API_KEY=your_gemini_key
```

3. Run the bot locally:

```bash
python bot.py
```

Commands available:

- `/doc` – отправить PDF/DOCX/изображение и получить текстовую выжимку;
- `/generate` – создать DOCX через Gemini по заданной теме;
- `/history` – список ранее обработанных файлов;
- `/risk`, `/review`, `/prompt` – демонстрационные ответы.
