import datetime

from django.db import models

class Ts(models.Model):
    class Done(models.TextChoices):
        DONE = 'd', 'Сделанно'
        NOT = 'n', 'Не сделанно'

    class When(models.Choices):
        ONE = 1, datetime.datetime.now()
        TWO = 2, datetime.datetime.now() + datetime.timedelta(days=1)
        THREE = 3, datetime.datetime.now() + datetime.timedelta(days=2)
        FOUR = 4, datetime.datetime.now() + datetime.timedelta(days=3)
        FIVE = 5, datetime.datetime.now() + datetime.timedelta(days=4)
        SIX = 6, datetime.datetime.now() + datetime.timedelta(days=5)
        SEVEN = 7, datetime.datetime.now() + datetime.timedelta(days=6)

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    date = models.DateField()
    done = models.CharField(max_length=1, choices=Done.choices, default=Done.NOT)

    def __str__(self):
        return f'{self.title}: {self.done}'