import os
import asyncio
from loguru import logger
from telegram_bot import build_app, schedule_jobs

TZ = os.getenv("TZ", "UTC")

async def main():
    try:
    app = await build_app()
    schedule_jobs(app)  # hourly jobs
    logger.info("QORA Alpha Core Starting (polling mode) | TZ={}", TZ)
    await app.run_polling(allowed_updates=None)
except Exception as e:
    logger.exception("Fatal error Starting QORA Alpha Core: {}", e)
    raise

if __name__ == "__main__":
    asyncio.run(main())
