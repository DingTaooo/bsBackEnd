from django.db import models
from datetime import datetime
from books.models import Books, Chapters
from circles.models import Circles
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class userFavBook(models.Model):
  """
  用户书架
  """
  user = models.ForeignKey(User, default="", on_delete=models.CASCADE, verbose_name="用户")
  books = models.ForeignKey(Books, default="", on_delete=models.CASCADE, verbose_name="图书 ")
  add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

  class Meta:
    verbose_name = '用户书架'
    verbose_name_plural = verbose_name
    unique_together = ("user", "books")

  def __str__(self):
    return self.user.name


class userCommentBook(models.Model):
  """
  用户评论图书
  """
  user = models.ForeignKey(User, default="", on_delete=models.CASCADE, verbose_name="用户")
  books = models.ForeignKey(Books, default="", on_delete=models.CASCADE, verbose_name="图书")
  comment_word = models.CharField(max_length=300, verbose_name="评论内容")
  score = models.PositiveSmallIntegerField(default=5, verbose_name="评分")
  add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间  ")

  class Meta:
    verbose_name = '用户书评'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.user.name


class userCommentChapter(models.Model):
  """
  用户评论章节
  """
  user = models.ForeignKey(User, default="", on_delete=models.CASCADE, verbose_name="用户")
  chapter = models.ForeignKey(Chapters, default="", on_delete=models.CASCADE, verbose_name="章节")
  comment_word = models.CharField(max_length=300, null=True, blank=True, verbose_name="评论内容")
  comment_image = models.ImageField(null=True, blank=True, verbose_name="评论图片", upload_to="circle/cirlceCommentImages")
  add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

  class Meta:
    verbose_name = '用户章节评论'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.user.name


class userLikeCircle(models.Model):
  """
  用户点赞畅想圈
  """
  user = models.ForeignKey(User, default="", verbose_name="用户", on_delete=models.CASCADE)
  circle = models.ForeignKey(Circles, default="", verbose_name="畅想圈", on_delete=models.CASCADE)
  add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

  class Meta:
    verbose_name = '用户点赞畅想圈'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.user.name

class userFellback(models.Model):
  '''
  用户反馈
  '''
  user = models.ForeignKey(User, default="", on_delete=models.CASCADE, verbose_name="用户")
  message = models.CharField(max_length=300, verbose_name="反馈内容")
  score = models.PositiveSmallIntegerField(default=5, verbose_name="小程序评分")
  add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

  class Meta:
    verbose_name = '用户反馈'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.user.name
