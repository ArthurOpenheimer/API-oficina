# Generated by Django 3.2.9 on 2021-12-04 03:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0022_auto_20211204_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='valor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='servico',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 12, 4, 0, 45, 22, 576719)),
        ),
    ]