from .serializers import BooksSerializers, ChaptersSerializers, BookCommentsSerializers, ExpandSerializers, AuthorsSerializers, TimelineSerializers, CharactersSerializers
from rest_framework import viewsets
from rest_framework import mixins
from .models import Books, Chapters, BookComments, Expand, Authors, Timeline, Characters
from .filters import BooksFilter, ChaptersFilter, BookCommentsFilter, ExpandFilter, AuthorsFilter, TimelineFilter, CharactersFilter
from django_filters.rest_framework import DjangoFilterBackend


class BooksListViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  展示图书
  '''
  queryset = Books.objects.all()
  serializer_class = BooksSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = BooksFilter


class ChaptersListViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  章节
  '''
  queryset = Chapters.objects.all()
  serializer_class = ChaptersSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = ChaptersFilter


class ExpandListViewset(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  扩展内容
  '''
  queryset = Expand.objects.all()
  serializer_class = ExpandSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = ExpandFilter

class BookCommentsListViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
  queryset = BookComments.objects.all()
  serializer_class = BookCommentsSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = BookCommentsFilter



class AuthorViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  作者
  '''
  queryset = Authors.objects.all()
  serializer_class = AuthorsSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = AuthorsFilter


class TimelineViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  时间轴
  '''
  queryset = Timeline.objects.all()
  serializer_class = TimelineSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = TimelineFilter


class CharactersViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  人物志
  '''
  queryset = Characters.objects.all()
  serializer_class = CharactersSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = CharactersFilter
