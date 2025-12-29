# Telegram bot (store + personal) quickstart

This folder contains a runnable Telegram bot that covers both store and personal life flows. It uses [`aiogram`](https://docs.aiogram.dev/) and in-memory service stubs you can replace with real APIs.

## Configuration
Set these environment variables (no secrets in git):

- `TELEGRAM_TOKEN` — Bot token from @BotFather.
- `BOT_OWNER_IDS` — Comma-separated Telegram user IDs allowed to run every command.
- `BOT_STAFF_IDS` — (Optional) IDs that can use store commands.
- `BOT_PERSONAL_IDS` — (Optional) IDs that can use personal commands.

Example `.env` snippet:

```
TELEGRAM_TOKEN=your-token-here
BOT_OWNER_IDS=12345678
BOT_STAFF_IDS=23456789,34567890
BOT_PERSONAL_IDS=12345678
```

> Keep the real token outside version control. Rotate it if you ever share or leak it.

## Run locally (long polling)

```
python -m bot.main
```

## Deployment notes
- For production, run behind HTTPS webhooks and a process supervisor.
- Replace the stub clients in `bot/store_services.py` and `bot/personal_services.py` with real integrations.
- Add background jobs (e.g., Celery/BullMQ) for digests and reminders to align with the monitoring plan in `docs/telegram_bot_irl.md`.
