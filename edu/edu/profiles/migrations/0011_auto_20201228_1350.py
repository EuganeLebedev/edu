# Generated by Django 3.1.4 on 2020-12-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20201228_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='group_code',
            field=models.ManyToManyField(to='profiles.StudentsGroupModel', verbose_name='Группа'),
        ),
    ]