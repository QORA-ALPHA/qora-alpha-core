# Placeholder for data connectors (CoinGecko, Yahoo Finance, NewsAPI, etc.)
# Implement async HTTP calls here using httpx and return normalized dicts.
import httpx

async def get_json(url: str, params: dict | None = None, timeout: float = 10.0):
    async with httpx.AsyncClient(timeout=timeout) as client:
        r = await client.get(url, params=params)
        r.raise_for_status()
        return r.json()
