# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-16 03:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2018, 5, 16, 3, 59, 53, 693305, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
