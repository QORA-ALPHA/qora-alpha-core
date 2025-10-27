# QORA Alpha Core
> Quantitative Observation & Rational Awareness — **Alpha Mode** ⚡

QORA Alpha Core is the central intelligence that powers **@QORA_Alpha_bot**.  
It analyzes global financial data, detects early market signals, and delivers real-time insights directly to Telegram.

## Features
- 🔍 Real-time financial monitoring
- 📰 News & sentiment scaffold
- 📈 Automated alerts with contextual breakdown
- 🎓 AI-driven educational insights
- 🌐 Multi-channel ready (Telegram first)

## Quickstart (Local)
1) Python 3.11+  
2) `cp .env.example .env` and set your values  
3) `pip install -r requirements.txt`  
4) `python main.py`

## Env Vars
```
TELEGRAM_BOT_TOKEN=xxxxxxxxxxxxxxxx
CHAT_ID=123456789  # optional default chat
TZ=UTC
```

## Commands (Telegram)
`/start` – welcome message  
`/activate` – enable hourly Alpha insights  
`/pause` – pause automatic alerts  
`/status` – show bot status  
`/alpha_report` – on-demand sample Alpha report

## Deploy on Render (Worker Service)
- Create a **Worker** service from this repo
- Command: `python main.py`
- Add env vars in Render dashboard
- Done. (Polling mode)

> For webhook mode, set up a web server (FastAPI) and call Telegram `setWebhook` with your HTTPS endpoint.
