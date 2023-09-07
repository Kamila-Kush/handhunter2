# Generated by Django 4.2.2 on 2023-09-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('founding_date', models.DateField(blank=True, null=True, verbose_name='Дата основания')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('number_of_employees', models.IntegerField(blank=True, null=True, verbose_name='Количество сотрудников')),
                ('is_hunting', models.BooleanField(default=True, verbose_name='Ищет сотрудников')),
                ('employee', models.ManyToManyField(blank=True, to='worker.worker', verbose_name='Работники')),
            ],
        ),
    ]
