# Generated by Django 3.1.4 on 2020-12-28 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20201117_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
