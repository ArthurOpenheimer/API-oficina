# Generated by Django 3.2.9 on 2021-12-04 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0023_auto_20211204_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 12, 4, 0, 54, 13, 31841)),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor',
            field=models.CharField(max_length=30),
        ),
    ]
