# Generated by Django 3.0.9 on 2020-08-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20200804_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='title_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
