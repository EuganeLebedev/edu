# Generated by Django 3.0.9 on 2020-08-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_title_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title_image',
            field=models.ImageField(default='courses_titles/empty.png', upload_to='courses_titles'),
        ),
    ]
