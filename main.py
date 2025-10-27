# main.py — QORA Alpha Core (Render / polling)

import os
import asyncio
from loguru import logger

# Importamos desde la raíz (porque telegram_bot.py está en la raíz del repo)
from telegram_bot import build_app, schedule_jobs

TZ = os.getenv("TZ", "UTC")

async def run():
    app = await build_app()          # crea la app de python-telegram-bot
    schedule_jobs(app)               # programa el job horario (HH:00)
    logger.info(f"QORA Alpha Core starting (polling mode) | TZ={TZ}")
    await app.run_polling(allowed_updates=None)

if name == "__main__":
    try:
        asyncio.run(run())
    except Exception as e:
        logger.exception(f"Fatal error starting QORA Alpha Core: {e}")
        raise
