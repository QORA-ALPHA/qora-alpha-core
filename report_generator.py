# report_generator.py — dummy report (reemplázalo si no existe)

from datetime import datetime, timezone

def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

async def build_alpha_report() -> str:
    title = "Market check: BTC & equities volatility watch"
    area = "#Crypto / #Equities"
    resumen = "BTC ~24h: n/a | Equities: n/a. Reuters headline integration coming next."
    ideas = [
        "Scale in on key supports; use staggered entries.",
        "Hedge tactically with cash/stablecoins if volatility expands.",
        "Rotate partially to infra plays if CEX stress emerges."
    ]
    sources = ["Reuters Markets (RSS)", "CoinGecko Simple Price API"]
    text = (
        "🚨 ALERT — QORA Alpha\n\n"
        f"📰 TITLE: {title}\n"
        f"📅 UTC: {now_utc()}\n"
        f"🌍 AREA: {area}\n\n"
        f"📋 SUMMARY:\n{resumen}\n\n"
        "💡 IDEAS:\n- " + "\n- ".join(ideas) + "\n\n"
        "🔗 SOURCES:\n- " + "\n- ".join(sources)
    )
    return text
