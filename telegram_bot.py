# telegram_bot.py — QORA Alpha Bot (root imports)

import os
import asyncio
from datetime import datetime, timezone

from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from report_generator import build_alpha_report  # <-- sin "src."

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DEFAULT_CHAT_ID = os.getenv("CHAT_ID")
ACTIVE = {"auto": True}

def utc_now_str():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Welcome to QORA Alpha — anticipation mode.\n\n"
        "Here, we don’t follow trends — we detect them before they form.\n\n"
        "Type /activate to start hourly Alpha insights, or /alpha_report to get one now."
    )
    await update.message.reply_text(text)

async def cmd_activate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ACTIVE["auto"] = True
    await update.message.reply_text("✅ Alpha mode activated (hourly insights).")

async def cmd_pause(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ACTIVE["auto"] = False
    await update.message.reply_text("⏸️ Alpha mode paused.")

async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Alpha auto: {ACTIVE['auto']} | Time: {utc_now_str()}")

async def cmd_alpha_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = await build_alpha_report()
    await update.message.reply_text(text, disable_web_page_preview=True)

async def push_alpha_report(app: Application):
    if not ACTIVE["auto"]:
        return
    text = await build_alpha_report()
    if DEFAULT_CHAT_ID:
        await app.bot.send_message(chat_id=int(DEFAULT_CHAT_ID), text=text, disable_web_page_preview=True)

def schedule_jobs(app: Application):
    scheduler = AsyncIOScheduler(timezone="UTC")
    scheduler.add_job(lambda: asyncio.create_task(push_alpha_report(app)), "cron", minute="0")
    scheduler.start()

async def build_app() -> Application:
    if not TOKEN:
        raise RuntimeError("Missing TELEGRAM_BOT_TOKEN env var")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("activate", cmd_activate))
    app.add_handler(CommandHandler("pause", cmd_pause))
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CommandHandler("alpha_report", cmd_alpha_report))
    return app
