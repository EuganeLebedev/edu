# Generated by Django 3.0.9 on 2020-08-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='title_image',
            field=models.ImageField(default=1, upload_to='courses_titles'),
            preserve_default=False,
        ),
    ]