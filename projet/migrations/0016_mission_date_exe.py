# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0015_auto_20160419_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='date_exe',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
