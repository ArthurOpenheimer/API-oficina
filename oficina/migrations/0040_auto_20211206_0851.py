# Generated by Django 3.2.9 on 2021-12-06 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0039_alter_servico_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='servico',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 12, 6, 8, 51, 9, 717385)),
        ),
    ]
