# src/main.py — QORA Alpha Core (Render-safe)

import os
import sys
import asyncio
from loguru import logger

# --- Asegurar imports desde la raíz del repo ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # .../project/src
ROOT_DIR = os.path.dirname(BASE_DIR)                    # .../project
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from telegram_bot import build_app, schedule_jobs  # archivo en la raíz

TZ = os.getenv("TZ", "UTC")

async def run_main():
    app = await build_app()
    schedule_jobs(app)
    logger.info(f"QORA Alpha Core starting (polling mode) | TZ={TZ}")
    await app.run_polling(allowed_updates=None)

def main():
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            logger.warning("Existing event loop detected; creating task...")
            loop.create_task(run_main())
        else:
            loop.run_until_complete(run_main())
    except Exception as e:
        logger.exception(f"Fatal error starting QORA Alpha Core: {e}")
        raise

if name == "__main__":  # <-- importante: dos guiones bajos
    main()
