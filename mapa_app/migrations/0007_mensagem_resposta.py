# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa_app', '0006_auto_20170510_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='resposta',
            field=models.CharField(choices=[('0', 'Não atendido'), ('1', 'Atendido')], default=2, max_length=1, verbose_name='Resposta'),
            preserve_default=False,
        ),
    ]
