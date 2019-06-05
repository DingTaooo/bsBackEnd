from rest_framework import serializers
from books.serializers import BooksSerializers
from .models import userFavBook, userCommentBook, userCommentChapter, userFellback, userLikeCircle
from users.serializers import UsersSerializers
from circles.serializers import AllCircleSerializers

class UsersBooksSerializers(serializers.ModelSerializer):
  # books = BooksSerializers()
  class Meta:
    model = userFavBook
    fields = ("books", "id", "user")

class UsersBookDetailSerializers(serializers.ModelSerializer):
  books = BooksSerializers()
  class Meta:
    model = userFavBook
    fields = "__all__"

class UserCommentBooksSerializers(serializers.ModelSerializer):
  user = UsersSerializers()
  add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
  class Meta:
    model = userCommentBook
    fields = "__all__"

class UserAddCommentBooksSerializers(serializers.ModelSerializer):
  class Meta:
    model = userCommentBook
    fields = ("books", "user", "comment_word", "score")

class UserCommentChapterSerializers(serializers.ModelSerializer):
  add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
  user = UsersSerializers()
  class Meta:
    model = userCommentChapter
    fields = "__all__"


class AddUserCommentChapterSerializers(serializers.ModelSerializer):
  class Meta:
    model = userCommentChapter
    fields = "__all__"


class UserLikeCircleSerializers(serializers.ModelSerializer):
  '''
  用户点赞Circle
  '''
  # add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
  class Meta:
    model = userLikeCircle
    fields = ("id", "user", "circle")

class UserLikeCircleDetailSerializers(serializers.ModelSerializer):
  '''
  用户点赞CircleDetail
  '''
  circle = AllCircleSerializers()
  # add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
  class Meta:
    model = userLikeCircle
    fields = ("id", "user", "circle")

class UserFellbackSerializers(serializers.ModelSerializer):
  '''
  用户反馈
  '''
  add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
  class Meta:
    model = userFellback
    fields = ("user", "message", "score", "add_time")