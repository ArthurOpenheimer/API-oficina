# Generated by Django 3.2.9 on 2021-12-06 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0044_alter_servico_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 12, 6, 14, 42, 5, 957224)),
        ),
    ]
