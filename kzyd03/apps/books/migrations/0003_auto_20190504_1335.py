# Generated by Django 2.2 on 2019-05-04 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190504_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapters',
            name='pub_time',
            field=models.DateTimeField(auto_now=True, verbose_name='发布时间'),
        ),
    ]
