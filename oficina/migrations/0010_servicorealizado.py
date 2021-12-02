# Generated by Django 3.2.9 on 2021-12-02 00:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0009_veiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicoRealizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=datetime.datetime(2021, 12, 1, 21, 20, 41, 217271))),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficina.funcionario')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficina.servico')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficina.veiculo')),
            ],
        ),
    ]
