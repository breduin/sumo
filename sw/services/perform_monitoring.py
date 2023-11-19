import asyncio
from loguru import logger

from common import Kakuzuke
from .fetch_data import fetch_data
from .messages import (
    get_formatted_bout_message,
    get_start_divizion_bouts_mesage,
    print_send_message,
    send_next_bout_message,
    )
from models import RikishiBout
from settings import SECONDS_TO_SLEEP_BETWEEN_REQUESTS
from utils import (
    clean_enclosed_dictionaries,
    )


def is_bout_over(bout: dict) -> bool:
    return int(bout['technic_id']) != -1


async def get_torikumi_data(day, kakuzuke_id):
    logger.info('Fetching data ...')
    basho_day = await fetch_data(day, kakuzuke_id)
    if not basho_day:
        logger.error('Даные не получены')
        return None
    logger.info('Received.')
    basho_day = clean_enclosed_dictionaries(basho_day)

    torikumi_data = basho_day.pop('TorikumiData')
    return torikumi_data


async def monitor_bouts(day: int, kakuzuke: Kakuzuke):
    '''Perform monitoring of bouts for given day and division.'''
    kakuzuke_id, kakuzuke_name = kakuzuke
    torikumi_data =  await get_torikumi_data(day, kakuzuke_id)
    bout_quantity = len(torikumi_data)
    current_bout_index = 0
    await asyncio.sleep(SECONDS_TO_SLEEP_BETWEEN_REQUESTS)
    next_bout = torikumi_data[0]
    send_next_bout_message(next_bout)

    while True:
        torikumi_data =  await get_torikumi_data(day, kakuzuke_id)
        bout = torikumi_data[current_bout_index]
        if not is_bout_over(bout):
            await asyncio.sleep(SECONDS_TO_SLEEP_BETWEEN_REQUESTS)
            continue

        east = bout.pop('east')
        west = bout.pop('west')

        east_rikishi = RikishiBout(**east)
        west_rikishi = RikishiBout(**west)
        message = get_formatted_bout_message(
            current_bout_index + 1,
            east_rikishi,
            west_rikishi,
            )

        print_send_message(message)
        current_bout_index += 1

        if current_bout_index == bout_quantity:
            break

        next_bout = torikumi_data[current_bout_index]
        if not is_bout_over(next_bout):
            await asyncio.sleep(3)  # respect Telegram requirements
            send_next_bout_message(next_bout)

    print_send_message(f'Bouts in {kakuzuke_name} finished.')


async def perform_daily_monitoring(day):
    for kakuzuke in [Kakuzuke.MAKUSHITA, Kakuzuke.JURYO, Kakuzuke.MAKUUCHI]:
        _, kakuzuke_name = kakuzuke
        logger.info(kakuzuke_name)
        message = get_start_divizion_bouts_mesage(kakuzuke_name)
        print_send_message(message)
        await monitor_bouts(day, kakuzuke)

    print_send_message(f'Bouts at Day {day} finished.')
