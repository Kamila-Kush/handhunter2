from django.db import models
from django.contrib.auth.models import User


class Worker(models.Model):
    user = models.OneToOneField(
        to=User,
        null=True, blank=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, verbose_name='Имя')
    specialization = models.CharField(max_length=255, verbose_name='Специализация')
    salary = models.IntegerField(null=True, blank=True, verbose_name='Желаемая зарплата')
    is_searching = models.BooleanField()

    def __str__(self):
        return self.name
