import os
import asyncio
from loguru import logger
from telegram_bot import build_app, schedule_jobs

TZ = os.getenv("TZ", "UTC")

async def main():
    app = await build_app()
    schedule_jobs(app)  # hourly jobs
    logger.info("Starting QORA Alpha Core (polling mode)...")
    await app.run_polling(allowed_updates=None)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
Fix import path for Render deployment
