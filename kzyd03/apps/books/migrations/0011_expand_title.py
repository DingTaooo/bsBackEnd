# Generated by Django 2.2 on 2019-05-15 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_remove_chapters_analyze'),
    ]

    operations = [
        migrations.AddField(
            model_name='expand',
            name='title',
            field=models.CharField(default='', max_length=300, verbose_name='标题'),
        ),
    ]
