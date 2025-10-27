# QORA Alpha Core — Main Runner (Render-compatible)

import os
import sys
import asyncio
from loguru import logger

# --- Path setup ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    from telegram_bot import build_app, schedule_jobs
except Exception as e:
    logger.error(f"Import error: {e}")
    raise

TZ = os.getenv("TZ", "UTC")

async def run_main():
    app = await build_app()
    schedule_jobs(app)
    logger.info(f"QORA Alpha Core starting (polling mode) | TZ={TZ}")
    await app.run_polling(allowed_updates=None)

def main():
    try:
        asyncio.run(run_main())
    except Exception as e:
        logger.exception(f"Fatal error starting QORA Alpha Core: {e}")
        raise

if __name__ == "__main__":
    main()
