# Generated by Django 3.0.9 on 2020-12-23 12:55

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20201202_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=256),
        ),
    ]
