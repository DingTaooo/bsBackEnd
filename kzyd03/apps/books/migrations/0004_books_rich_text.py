# Generated by Django 2.2 on 2019-05-04 05:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190504_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='rich_text',
            field=ckeditor.fields.RichTextField(default='', verbose_name='rich_text_demo'),
        ),
    ]
