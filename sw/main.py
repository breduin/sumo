import asyncio
import httpx
import json

from loguru import logger

from services import perform_daily_monitoring
from settings import BACKEND_NEXT_TIME_POINT_URL


logger.add(
    'logs/sumo.log',
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    rotation="5 MB"
    )


async def main():
    '''Ask backend for sleeping time and run daily monitoring.'''
    while True:
        async with httpx.AsyncClient() as client:
            try:
                r = await client.get(BACKEND_NEXT_TIME_POINT_URL)
            except httpx.ConnectError:
                await asyncio.sleep(5)
                continue
        if r.status_code != httpx.codes.OK:
            logger.error(f'Next time point request error {r.status_code}')
            await asyncio.sleep(30)
            continue
        next_point = json.loads(r.text)
        day = next_point['day']
        sleep_seconds = next_point['sleep_seconds']
        logger.info(f'Next monitoring starts in {sleep_seconds} seconds')

        await asyncio.sleep(sleep_seconds)

        await perform_daily_monitoring(day)


if __name__ == "__main__":
    try:
        logger.info('Monitoring started')
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info('Monitoring stopped')
