# Generated by Django 2.2 on 2019-05-14 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20190512_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcomments',
            name='comment_comment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comment_for_this_comment', to='books.BookComments', verbose_name='图书评论'),
        ),
    ]