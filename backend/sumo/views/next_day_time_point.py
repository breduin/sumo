from dataclasses import dataclass, field
from datetime import datetime, time, timedelta, timezone

from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@dataclass
class Basho:
    start = datetime.fromisoformat('2024-01-14T00:00:00+03:00')
    finish = datetime.fromisoformat('2024-01-28T00:00:00+03:00')


@dataclass
class Start:
    now: datetime
    in_one_week: int = 60 * 60 * 24 * 7
    immidiately: int = 0
    tomorrow_at_7am: int = field(init=False)
    today_at_7am: int = field(init=False)

    def __post_init__(self):
        self.tomorrow_at_7am = (
            datetime.combine(
                self.now.date() + timedelta(days=1),
                time(7, 0, tzinfo=timezone(timedelta(hours=3)))
                ) - self.now
        ).seconds
        self.today_at_7am = (
            datetime.combine(
                self.now.date(),
                time(7, 0, tzinfo=timezone(timedelta(hours=3)))
                ) - self.now
                ).seconds


def get_day_and_seconds(basho):
    '''Return day number and seconds number to next monitoring start.'''
    now = datetime.now(tz=timezone(timedelta(hours=3)))
    start = Start(now)
    basho_days_number = (basho.finish - basho.start).days + 1
    if not basho.start <= now <= basho.finish:  # ask again in one week
        day_number = -1
        return day_number, start.in_one_week

    day_number = (now - basho.start).days + 1
    if now.hour >= 12:
        if day_number + 1 > basho_days_number:
            return -1, start.in_one_week
        return day_number + 1, start.tomorrow_at_7am
    if now.hour >= 7:
        return day_number, start.immidiately

    return day_number, start.today_at_7am


@method_decorator(csrf_exempt, name='dispatch')
class NextDayTimePointView(View):
    def get(self, request, *args, **kwargs):
        basho = Basho()
        day, sleep_seconds = get_day_and_seconds(basho)
        next_point = {
            'day': day,
            'sleep_seconds': sleep_seconds
            }
        return JsonResponse(next_point)
