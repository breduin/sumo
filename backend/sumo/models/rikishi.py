'''Модель для рикиси (сумотори) - бойца сумо'''
from django.db import models
from common import TimeStampedModel
from .abstracts import Person
from .shikona import Shikona


class Rikishi(TimeStampedModel, Person):

    rikishi_external_id = models.PositiveIntegerField(
        help_text="Rikishi's ID at the Nihon Sumo Kyokai database"
        )
    shikona = models.ForeignKey(
        Shikona,
        on_delete=models.CASCADE,
        verbose_name='current ring name'
        )

    def update_shikona(self):
        pass

    def update_win_lose(self):
            pass
