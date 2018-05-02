# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-02 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
