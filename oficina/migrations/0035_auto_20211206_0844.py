# Generated by Django 3.2.9 on 2021-12-06 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0034_alter_servico_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 12, 6, 8, 44, 7, 726481)),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor',
            field=models.CharField(max_length=30),
        ),
    ]
