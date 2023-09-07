from django.db import models
from worker.models import Worker

class Company(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    founding_date = models.DateField(null=True, blank=True, verbose_name='Дата основания')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Адрес')
    number_of_employees = models.IntegerField(null=True, blank=True, verbose_name='Количество сотрудников')
    is_hunting = models.BooleanField(default=True, verbose_name='Ищет сотрудников')
    employee = models.ManyToManyField(
        to=Worker,
        blank=True,
        verbose_name='Работники'
    )

    def __str__(self):
        return self.title


