# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0002_auto_20160316_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missionobs',
            name='mission',
        ),
        migrations.AddField(
            model_name='mission',
            name='etat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mission',
            name='observation',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='MissionObs',
        ),
    ]