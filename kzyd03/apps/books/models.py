# encoding: utf-8

from django.db import models
# from users.models import UserProfile
from ckeditor.fields import RichTextField


# 评论功能先不要写
# 后期可再加功能：书籍评分，章节评分

# Create your models here.
class Authors(models.Model):
  """
  作者
  """
  author_id = models.AutoField(primary_key=True, verbose_name="作者编号")
  name = models.CharField(max_length=30, null=True, blank=True, verbose_name="作者")
  author_image = models.ImageField(max_length=200, default="", upload_to="book/authorImage/", verbose_name="作者图片")
  intro = models.TextField(verbose_name="作者介绍")
  time = models.CharField(max_length=50, default="", verbose_name="生卒年")

  class Meta:
    verbose_name = '作者'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name


class Books(models.Model):
  """
  图书
  """
  book_id = models.AutoField(primary_key=True, verbose_name="书籍编号")
  name = models.CharField(max_length=30, null=True, blank=True, verbose_name="书名")
  book_type = models.IntegerField(default="1", verbose_name="分类")
  cover_image = models.ImageField(max_length=200, upload_to="book/coverImage/", verbose_name="封面图")
  pub_time = models.DateField(null=True, blank=True, verbose_name="出版时间")
  intro = models.TextField(verbose_name="图书介绍")
  labal = models.CharField(max_length=20, default='', verbose_name="标签")
  authors = models.ManyToManyField(to='Authors', verbose_name="作者")
  is_recommend = models.BooleanField(default=False, verbose_name="推荐")
  editors_id = models.CharField(max_length=30, verbose_name="再创作者")
  is_new = models.BooleanField(default=False, verbose_name="最新")

  class Meta:
    verbose_name = '图书'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name


class Chapters(models.Model):
  """
  章节
  """
  chapter_id = models.AutoField(primary_key=True, verbose_name="章节编号")
  name = models.CharField(max_length=30, null=True, blank=True, verbose_name="章节名")
  pub_time = models.DateTimeField(auto_now=True, verbose_name="发布时间")
  # 章节内容和解析应该用富文本 先用TextField
  article = RichTextField(verbose_name="章节内容")
  # analyze = RichTextField(verbose_name="解析")
  # article = models.TextField(verbose_name="章节内容")
  # analyze = models.TextField(verbose_name="解析")
  like_num = models.IntegerField(default="0", verbose_name="点赞数")
  is_read = models.BooleanField(default=False, verbose_name="是否读过")
  book = models.ForeignKey(Books, default="", on_delete=models.CASCADE, related_name="this_chapter_from_this_book",
                           verbose_name="所属书籍")

  class Meta:
    verbose_name = '章节'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name

class Expand(models.Model):
  '''
  章节拓展
  '''
  title = models.CharField(max_length=300, default="", verbose_name="标题")
  content = models.TextField(null=True, blank=True, verbose_name="扩展内容")
  image = models.ImageField(null=True, blank=True, upload_to="book/chapterExpandImages", verbose_name="相关图片")
  chapter = models.ForeignKey(Chapters, default="", on_delete=models.CASCADE, verbose_name="所属章节")

  class Meta:
    verbose_name = '章节拓展'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.content

class BookComments(models.Model):
  """
  书评
  """
  creare_time = models.DateTimeField(auto_now_add=True)
  comment_word = models.TextField(verbose_name='评论内容')
  like_num = models.IntegerField(default="0", verbose_name="点赞数")
  # creater = models.ForeignKey(UserProfile, related_name="comment_from_this_user", default="", verbose_name="评论者",
  #                             on_delete=models.CASCADE)外键用户不可行
  comment_book = models.ForeignKey(Books, related_name="comment_for_this_book", default="", verbose_name="图书评论",
                                   on_delete=models.CASCADE)
  comment_comment = models.ForeignKey('self', related_name="comment_for_this_comment", null=True, blank=True, default="", verbose_name="评论评论",
                                   on_delete=models.CASCADE)

  class Meta:
    verbose_name = '书评'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.comment_word


class ChapterComments(models.Model):
  """
  章节评论
  """
  creare_time = models.DateTimeField(auto_now_add=True)
  comment_word = models.TextField(verbose_name="评论内容")
  like_num = models.IntegerField(default="0", verbose_name="点赞数")
  comment_image = models.ImageField(null=True, blank=True, upload_to="book/chapterCommentImages", verbose_name="评论图片")
  # creater = models.ForeignKey(Chapters, related_name="comment_from_this_user", default="", verbose_name="评论者",
  #                             on_delete=models.CASCADE)
  comment_chapter = models.ForeignKey(Chapters, default="", related_name="comment_for_this_chapter",
                                      verbose_name="章节评论",
                                      on_delete=models.CASCADE, )

  class Meta:
    verbose_name = '章节评论'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.comment_word


class Timeline(models.Model):
  '''
  时间线
  '''
  time = models.CharField(max_length=300, default="", verbose_name="时间点")
  title = models.CharField(max_length=30, default="", verbose_name="标题")
  image = models.ImageField(null=True, blank=True, upload_to="book/timelineImages", verbose_name="相关图片")
  intro = models.TextField(verbose_name="内容")
  book = models.ForeignKey(Books, default="", on_delete=models.CASCADE, related_name="this_timeline_from_this_book",
                           verbose_name="所属书籍")

  class Meta:
    verbose_name = '时间线'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.book.name + ":" +self.title

class Characters(models.Model):
  '''
  人物志
  '''
  name = models.CharField(max_length=300, default="", verbose_name="姓名")
  title = models.CharField(max_length=30, default="", verbose_name="标题")
  image = models.ImageField(null=True, blank=True, upload_to="book/charactersImages", verbose_name="相关图片")
  intro = models.TextField(verbose_name="内容")
  book = models.ForeignKey(Books, default="", on_delete=models.CASCADE, related_name="this_characters_from_this_book",
                           verbose_name="所属书籍")

  class Meta:
    verbose_name = '人物志'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.book.name + ":" +self.name