import django_filters
from django.db.models import Q

from .models import Books, Chapters, BookComments, Expand, Authors, Timeline, Characters


class BooksFilter(django_filters.rest_framework.FilterSet):
  """
  过滤书籍
  """
  name = django_filters.CharFilter(lookup_expr='icontains')
  book_id = django_filters.CharFilter()

  class Meta:
    model = Books
    fields = ['name', 'book_id', 'book_type']


class ChaptersFilter(django_filters.rest_framework.FilterSet):
  """
  过滤章节
  """

  class Meta:
    model = Chapters
    fields = ['book', 'chapter_id']

class ExpandFilter(django_filters.rest_framework.FilterSet):
  """
  过滤章节扩展
  """

  class Meta:
    model = Expand
    fields = ['chapter']


class BookCommentsFilter(django_filters.rest_framework.FilterSet):
  """
  过滤书评
  """
  # book_id = django_filters.CharFilter()

  class Meta:
    model = BookComments
    fields = ['comment_book']

class AuthorsFilter(django_filters.rest_framework.FilterSet):
  """
  过滤作者
  """
  # book_id = django_filters.CharFilter()

  class Meta:
    model = Authors
    fields = ['author_id']

class TimelineFilter(django_filters.rest_framework.FilterSet):
  """
  过滤时间线
  """

  class Meta:
    model = Timeline
    fields = ['book']

class CharactersFilter(django_filters.rest_framework.FilterSet):
  """
  过滤人物志
  """

  class Meta:
    model = Characters
    fields = ['book']
