import asyncio
import httpx

from settings import SUMO_DATA_URL


async def fetch_data(day: int, kakuzuke_id: int) -> dict:
    attempts = 10
    attempt = 1
    async with httpx.AsyncClient() as client:
        data = None
        while attempt <= attempts:
            try:
                sumo_url = f'{SUMO_DATA_URL}/{kakuzuke_id}/{day}/'
                response = await client.get(sumo_url)
                data = response.json()
                break
            except Exception:
                await asyncio.sleep(2 * attempt)
                attempt += 1
                continue
        return data
