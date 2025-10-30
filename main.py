import os
from datetime import datetime, timezone
from typing import Dict, Any
from fastapi import FastAPI, HTTPException
import httpx

TELEGRAM_TOKEN = os.getenv("NEWS_SCAVENGER_BOT","")
WEBHOOK_SECRET_PATH = os.getenv("whk-2fQh7jPgJ9ZkR0yE6vT3wB1m","")
BOT_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True, "time": datetime.now(timezone.utc).isoformat()}

async def tg_send(chat_id: int, text: str):
    if not TELEGRAM_TOKEN: return
    async with httpx.AsyncClient(timeout=15) as client:
        await client.post(f"{BOT_API}/sendMessage",
                          json={"chat_id": chat_id, "text": text})

@app.post("/webhook/{secret_path}")
async def webhook(secret_path: str, payload: Dict[str, Any]):
    if secret_path != WEBHOOK_SECRET_PATH:
        raise HTTPException(status_code=403, detail="forbidden")
    msg = payload.get("message") or {}
    chat_id = (msg.get("chat") or {}).get("id")
    txt = (msg.get("text") or "").strip()
    if not chat_id: return {"ok": True}
    if txt.startswith("/start"):
        await tg_send(chat_id, "Suscripción activa ✅")
    elif txt.startswith("/stop"):
        await tg_send(chat_id, "Suscripción cancelada.")
    else:
        await tg_send(chat_id, "Comandos: /start /stop")
    return {"ok": True}
