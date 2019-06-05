import django_filters
from django.db.models import Q

from .models import userFavBook, userCommentBook, userCommentChapter, userFellback, userLikeCircle


class UsersBooksFilter(django_filters.rest_framework.FilterSet):
  """
  获取用户书架
  """

  class Meta:
    model = userFavBook
    fields = ['user']


class UserCommentBooksFilter(django_filters.rest_framework.FilterSet):
  """
  用户评论图书
  """

  class Meta:
    model = userCommentBook
    fields = ['user', 'books']


class UserCommentChaptersFilter(django_filters.rest_framework.FilterSet):
  """
  用户评论章节
  """
  class Meta:
    model = userCommentChapter
    fields = ['user', 'chapter']

class UserLikeCircleFilter(django_filters.rest_framework.FilterSet):
  """
  用户评论章节
  """
  class Meta:
    model = userLikeCircle
    fields = ['user', 'circle']


class UserFellbackFilter(django_filters.rest_framework.FilterSet):
  """
  用户评论章节
  """
  class Meta:
    model = userFellback
    fields = ['user']

