# Generated by Django 2.2 on 2019-05-16 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_userlikecircle'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercommentchapter',
            name='comment_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='评论图片'),
        ),
    ]
