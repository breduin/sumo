from bot import bot
from common import BoutResults
from models import RikishiBout
from settings import TG_CHAT_ID


def get_formatted_bout_message(
        bout_number: int,
        east_rikishi: RikishiBout,
        west_rikishi: RikishiBout
        ) -> str:
    bout_result_east = BoutResults.WINNER if east_rikishi.result_image == 'result_ic01.gif' else BoutResults.LOSER
    bout_result_west = BoutResults.get_opposite(bout_result_east)
    output_bout_number = f'Bout №{bout_number}'

    output_east_rikishi = f'{east_rikishi.shikona_eng} ({bout_result_east})'
    output_west_rikishi = f'{west_rikishi.shikona_eng} ({bout_result_west})'
    str_length = max(len(output_east_rikishi), len(output_west_rikishi))
    output_rikishi = "{:>{}} - {:<{}}".format(
        output_east_rikishi,
        str_length + 1,
        output_west_rikishi,
        str_length + 1,
        )

    output_east_rikishi_rank = f'{east_rikishi.banzuke_name_eng}'
    output_west_rikishi_rank = f'{west_rikishi.banzuke_name_eng}'
    output_rank = "{:>{}} - {:<{}}".format(
        output_east_rikishi_rank,
        str_length + 1,
        output_west_rikishi_rank,
        str_length + 1,
        )

    output_east_rikishi_wl = f'{east_rikishi.won_number}/{east_rikishi.lost_number}'
    output_west_rikishi_wl = f'{west_rikishi.won_number}/{west_rikishi.lost_number}'
    output_rikishi_wl = "{:>{}} - {:<{}}".format(
        output_east_rikishi_wl,
        str_length + 1,
        output_west_rikishi_wl,
        str_length + 1,
        )
    message = '\n'.join(
        [
            output_bout_number,
            output_rank,
            output_rikishi,
            output_rikishi_wl,
            ]
            )
    return message


def get_start_divizion_bouts_mesage(kakuzuke: str) -> str:
    message = f'Start bouts in {kakuzuke} division'
    return message


def get_next_bout_mesage(bout: dict) -> str:
    next_bout_text = "Next bout:"
    next_rikishi_text = f"{bout['east']['shikona_eng']} ({bout['east']['banzuke_name_eng']}) - {bout['west']['shikona_eng']} ({bout['west']['banzuke_name_eng']})"
    message = '\n'.join(
        [
            next_bout_text,
            next_rikishi_text
        ]
        )
    return message


def print_send_message(message):
    print(message)
    bot.send_message(
        chat_id=TG_CHAT_ID,
        text=message,
        )

def send_next_bout_message(bout: dict) -> None:
    message = get_next_bout_mesage(bout)
    print_send_message(message)
