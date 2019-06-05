from django.db import models
from django.contrib.auth.models import AbstractUser

from books.models import Books


# Create your models here.
class UserProfile(AbstractUser):
  name = models.CharField(max_length=30, default="user", verbose_name="姓名")
  user_image = models.ImageField(max_length=200, default="", upload_to="user/userImages/", verbose_name="用户头像")
  phone = models.CharField(max_length=11, verbose_name="电话")
  password = models.CharField(max_length=300, verbose_name="密码")
  books = models.ManyToManyField(Books, default="", related_name="user_fav_books", verbose_name="书架")
  edit_books = models.ManyToManyField(Books, default="", related_name="user_reediter_books", verbose_name="编辑的书籍")
  is_author = models.BooleanField(default=False, verbose_name="编辑")

  class Meta:
    verbose_name = '用户'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name
