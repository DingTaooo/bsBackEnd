from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# from users.models import UserProfile

# Create your models here.
class Circles(models.Model):
  """
  畅想圈
  """
  circle_id = models.AutoField(primary_key=True, verbose_name="畅想编号")
  # sub_man = models.CharField(max_length=30, verbose_name="作者")
  sub_man = models.ForeignKey(User, default="", on_delete=models.CASCADE, verbose_name="用户")
  creare_time = models.DateTimeField(auto_now=True, verbose_name="发布时间")
  desc = models.TextField(default="", verbose_name="描述")
  image = models.ImageField(upload_to="circle/images/", null=True, blank=True, verbose_name="图片")
  like_num = models.IntegerField(default=0, verbose_name="点赞数")
  comment_num = models.IntegerField(default=0, verbose_name="评论数")

  class Meta:
    verbose_name = '畅想圈'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.sub_man.name + ":" + self.desc


class Comments(models.Model):
  """
  创想圈评论
  """
  # user_id = models.CharField(max_length=30, default="", verbose_name="评论者编号")
  creare_time = models.DateTimeField(auto_now_add=True, verbose_name="提交时间")
  sub_man = models.ForeignKey(User, default="", on_delete=models.CASCADE, verbose_name="用户")
  # user_name = models.CharField(max_length=100, default="", verbose_name="用户名称")
  comment_word = models.TextField(verbose_name="评论内容")
  like_num = models.IntegerField(default="0", verbose_name="点赞数")
  # 这里comment_chapter写错了，应该是comment_circle，目前不敢改。
  comment_chapter = models.ForeignKey(Circles, default="", related_name="comment_for_this_circle", verbose_name="动态评论",
                                      on_delete=models.CASCADE, )

  class Meta:
    verbose_name = '畅想圈评论'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.comment_word
