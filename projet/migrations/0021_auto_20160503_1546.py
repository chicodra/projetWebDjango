# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0020_auto_20160503_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programme',
            name='com',
        ),
        migrations.AddField(
            model_name='programme',
            name='com',
            field=models.ManyToManyField(to='projet.Commercial'),
        ),
    ]
