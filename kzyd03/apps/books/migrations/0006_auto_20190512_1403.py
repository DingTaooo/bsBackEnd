# Generated by Django 2.2 on 2019-05-12 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20190512_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_type',
            field=models.IntegerField(default='1', verbose_name='分类'),
        ),
    ]