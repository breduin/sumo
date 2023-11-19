from django.db import models


class Person(models.Model):
    '''Abstract class for persons.'''
    first_name = models.CharField(
        max_length=128,
        verbose_name='first name',
        blank=True,
        )
    last_name = models.CharField(
        max_length=128,
        verbose_name='last name',
        blank=True,
        )
    birth_date = models.DateField(
        verbose_name='date of birth',
        blank=True,
        null=True,
        )
    birth_place = models.CharField(
        verbose_name='place of birth',
        blank=True,
        )

    class Meta:
        abstract = True
