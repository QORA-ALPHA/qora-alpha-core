# main.py — QORA Alpha Core (Render / polling)

import os
import asyncio
from loguru import logger

from telegram_bot import build_app, schedule_jobs  # importa desde la raíz

TZ = os.getenv("TZ", "UTC")

async def run():
    app = await build_app()
    schedule_jobs(app)
    logger.info(f"QORA Alpha Core starting (polling mode) | TZ={TZ}")
    await app.run_polling(allowed_updates=None)

if name == "__main__":
    try:
        asyncio.run(run())
    except Exception as e:
        logger.exception(f"Fatal error starting QORA Alpha Core: {e}")
        raise
