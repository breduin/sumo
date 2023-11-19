'''Utilities for the project.'''
import html
import re

from datetime import datetime


def clean_enclosed_dictionaries(data: dict) -> dict:
    '''Recoursively clean dictionary of html symbols like &nbsp;'''
    for key, value in data.items():
        if isinstance(value, dict):
            clean_enclosed_dictionaries(value)
        elif isinstance(value, str):
            value = html.unescape(value)
            data[key] = value
    return data


def extract_date(data: dict) -> str:
    '''Extract date'''
    pattern = r"((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4})"

    text = data['dayHead']
    match = re.search(pattern, text)

    if match:
        received_date_format = "%B %d, %Y"
        received_date = datetime.strptime(match.group(1), received_date_format).date()
        return received_date.strftime("%Y-%m-%d")

    return ''
