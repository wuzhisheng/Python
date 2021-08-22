# Generated by Django 2.0.8 on 2019-01-17 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190117_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'db_table': 'dept2',
            },
        ),
        migrations.CreateModel(
            name='Employee2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('province', models.CharField(max_length=32)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Dept')),
            ],
            options={
                'db_table': 'employee2',
            },
        ),
    ]
