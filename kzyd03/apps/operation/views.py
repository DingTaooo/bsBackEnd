from .serializers import UsersBooksSerializers, UserCommentBooksSerializers, UserAddCommentBooksSerializers, UserCommentChapterSerializers, UsersBookDetailSerializers, UserFellbackSerializers, UserLikeCircleSerializers, UserLikeCircleDetailSerializers, AddUserCommentChapterSerializers
from rest_framework import viewsets
from rest_framework import mixins
from .models import userFavBook, userCommentBook, userCommentChapter, userFellback, userLikeCircle
from .filters import UsersBooksFilter, UserCommentBooksFilter, UserCommentChaptersFilter, UserFellbackFilter, UserLikeCircleFilter
from django_filters.rest_framework import DjangoFilterBackend


class UsersBooksListViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  用户书架
  '''
  queryset = userFavBook.objects.all()
  serializer_class = UsersBooksSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = UsersBooksFilter

class UsersBookDetailListViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  用户书架详情
  '''
  queryset = userFavBook.objects.all()
  serializer_class = UsersBookDetailSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = UsersBooksFilter

class UserCommentBooksListViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
  queryset = userCommentBook.objects.all().order_by('-add_time')
  serializer_class = UserCommentBooksSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = UserCommentBooksFilter

class UserAddCommentBooksListViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
  queryset = userCommentBook.objects.all()
  serializer_class = UserAddCommentBooksSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = UserCommentBooksFilter

class UserCommentChapterListViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
  queryset = userCommentChapter.objects.all().order_by('-add_time')
  serializer_class = UserCommentChapterSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = UserCommentChaptersFilter

class AddUserCommentChapterListViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
  queryset = userCommentChapter.objects.all()
  serializer_class = AddUserCommentChapterSerializers
  # filter_backends = (DjangoFilterBackend,)
  # filter_class = UserCommentChaptersFilter

class UserLikeCircleViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  用户点赞Circles
  '''
  queryset = userLikeCircle.objects.all()
  serializer_class = UserLikeCircleSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = UserLikeCircleFilter

class UserLikeCircleDetailViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  用户点赞CirclesDetail
  '''
  queryset = userLikeCircle.objects.all()
  serializer_class = UserLikeCircleDetailSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = UserLikeCircleFilter

class UserFellbackViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
  '''
  用户反馈
  '''
  queryset = userFellback.objects.all()
  serializer_class = UserFellbackSerializers
  filter_backends = (DjangoFilterBackend,)
  filter_class = UserFellbackFilter