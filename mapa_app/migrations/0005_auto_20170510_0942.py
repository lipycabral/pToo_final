# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapa_app', '0004_local_codusuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datamensagem', models.DateTimeField()),
                ('mensagem', models.TextField(blank=True, null=True, verbose_name='Mensagem')),
                ('codchamado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapa_app.Local')),
            ],
            options={
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
            },
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
    ]
