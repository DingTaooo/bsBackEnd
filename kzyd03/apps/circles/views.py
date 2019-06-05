from .serializers import CirclesSerializers, AllCircleSerializers, CircleCommentSerializers, AllCircleCommentSerializers
from rest_framework import viewsets
from rest_framework import mixins
from .models import Circles, Comments
from .filters import CirclesFilter, CircleCommentFilter
from django_filters.rest_framework import DjangoFilterBackend

# 新增Circle
class CirclesListViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
  queryset = Circles.objects.all()
  serializer_class = CirclesSerializers
  # filter_backends = (DjangoFilterBackend,)
  # filter_class = CirclesFilter



class AllCirclesViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  获取全部Circle
  '''
  queryset = Circles.objects.all().order_by('-creare_time')
  serializer_class = AllCircleSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = CirclesFilter


class CircleCommentViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  获取circle评论
  '''
  queryset = Comments.objects.all()
  serializer_class = CircleCommentSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = CircleCommentFilter

class AllCircleCommentViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  获取circle评论
  '''
  queryset = Comments.objects.all().order_by('-creare_time')
  serializer_class = AllCircleCommentSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = CircleCommentFilter


