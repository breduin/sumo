'''Модель для сиконы - имени борца на ринге.'''
from django.db import models
from common import TimeStampedModel


class Shikona(TimeStampedModel):
    '''Shikona - rikoshi ring name.'''
    name = models.CharField(
        max_length=128,
        verbose_name='shikona (eng)',
        help_text="Rikishi's ring name"
        )
    name_jp = models.CharField(
        max_length=128,
        verbose_name='shikona (jp)',
        help_text="Rikishi's ring name in Japaneese",
        blank=True,
        )
    date = models.DateField(
        verbose_name='date the shikona is assigned',
        blank=True,
        null=True,
        )
    is_default = models.BooleanField(
        verbose_name='Default shikona?',
        default=False,
        )
