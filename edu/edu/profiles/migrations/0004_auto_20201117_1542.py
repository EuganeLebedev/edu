# Generated by Django 3.0.9 on 2020-11-17 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200929_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsGroup',
            fields=[
                ('group_code', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='group_code',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='phone_number',
            field=models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator(message='Формат телефонного номера должен быть +99999999', regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='group_code',
            field=models.ManyToManyField(to='profiles.StudentsGroup', verbose_name='group'),
        ),
    ]
