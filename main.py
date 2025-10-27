# main.py — QORA Alpha Core (Render-safe asyncio)

import os
import asyncio
from loguru import logger
from telegram_bot import build_app, schedule_jobs

TZ = os.getenv("TZ", "UTC")

async def run_main():
    app = await build_app()
    schedule_jobs(app)
    logger.info(f"QORA Alpha Core starting (polling mode) | TZ={TZ}")
    await app.run_polling(allowed_updates=None)

def main():
    try:
        # Usamos el event loop existente si ya está activo (Render safe)
        loop = asyncio.get_event_loop()
        if loop.is_running():
            logger.warning("Existing event loop detected, creating new task...")
            loop.create_task(run_main())
        else:
            loop.run_until_complete(run_main())
    except Exception as e:
        logger.exception(f"Fatal error starting QORA Alpha Core: {e}")
        raise

if name == "__main__":
    main()
