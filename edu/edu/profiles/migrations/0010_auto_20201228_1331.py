# Generated by Django 3.1.4 on 2020-12-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_studentsgroupmodel_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='group_code',
            field=models.ManyToManyField(related_name='users', to='profiles.StudentsGroupModel', verbose_name='Группа'),
        ),
    ]
