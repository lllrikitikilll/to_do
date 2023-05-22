import datetime
from django.core import validators
from django.db import models

class Ts(models.Model):
    class Done(models.TextChoices):
        DONE = 'd', 'Сделанно'
        NOT = 'n', 'Не сделанно'

    title = models.CharField(max_length=150, verbose_name='Задача', validators=[validators.MinLengthValidator(2, message='Введите более 2 символов')])
    description = models.TextField(blank=True, verbose_name='Описание')
    date = models.DateField(verbose_name='Дата выполнения')
    done = models.CharField(max_length=1, choices=Done.choices, default=Done.NOT, verbose_name="Статус")

    def __str__(self):
        return f'{self.title}: {self.done}'

