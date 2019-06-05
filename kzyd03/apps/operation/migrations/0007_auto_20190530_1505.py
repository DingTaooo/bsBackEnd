# Generated by Django 2.2 on 2019-05-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0006_usercommentchapter_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercommentchapter',
            name='comment_image',
            field=models.ImageField(blank=True, null=True, upload_to='circle/cirlceCommentImages', verbose_name='评论图片'),
        ),
        migrations.AlterField(
            model_name='usercommentchapter',
            name='comment_word',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='评论内容'),
        ),
    ]
