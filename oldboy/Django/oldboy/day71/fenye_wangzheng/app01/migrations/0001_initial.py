# Generated by Django 2.0.8 on 2019-01-17 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('province', models.CharField(max_length=32)),
                ('dept', models.CharField(max_length=16)),
            ],
        ),
    ]
