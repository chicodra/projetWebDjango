# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0013_auto_20160415_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='mission',
            name='programme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projet.Programme'),
        ),
        migrations.AddField(
            model_name='mission',
            name='TypeMission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projet.TypeMission'),
        ),
    ]
