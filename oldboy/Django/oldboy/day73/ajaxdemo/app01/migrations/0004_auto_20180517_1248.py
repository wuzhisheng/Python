# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-17 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_userinfo_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='mobile',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
