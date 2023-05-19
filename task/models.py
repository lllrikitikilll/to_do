import datetime

from django.db import models

class Ts(models.Model):
    class Done(models.TextChoices):
        DONE = 'd', 'Сделанно'
        NOT = 'n', 'Не сделанно'

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    date = models.DateField()
    done = models.CharField(max_length=1, choices=Done.choices, default=Done.NOT)

    def __str__(self):
        return f'{self.title}: {self.done}'
