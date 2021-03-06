# Generated by Django 3.2.9 on 2021-12-03 22:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0014_auto_20211203_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 12, 3, 19, 24, 0, 268435)),
        ),
        migrations.AddField(
            model_name='servico',
            name='funcionario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='oficina.funcionario'),
        ),
        migrations.AddField(
            model_name='servico',
            name='veiculo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='oficina.veiculo'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='cliente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='oficina.cliente'),
        ),
        migrations.DeleteModel(
            name='ServicoRealizado',
        ),
    ]
