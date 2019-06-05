from rest_framework import serializers
from .models import Circles, Comments
from users.serializers import UsersSerializers
from rest_framework import status


class CirclesSerializers(serializers.ModelSerializer):
  # sub_man = UsersSerializers()
  creare_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
  class Meta:
    model = Circles
    fields= ("sub_man", "desc", "image", "creare_time")

class AllCircleSerializers(serializers.ModelSerializer):
  sub_man = UsersSerializers()
  creare_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
  class Meta:
    model = Circles
    fields= ("__all__")

class CircleCommentSerializers(serializers.ModelSerializer):
  # sub_man = UsersSerializers()
  creare_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
  class Meta:
    model = Comments
    fields= ("comment_word", "sub_man", "comment_chapter", "creare_time")
    # 还要写一个获取用户信息的AllCircleCommentSerializers

class AllCircleCommentSerializers(serializers.ModelSerializer):
  sub_man = UsersSerializers()
  creare_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
  class Meta:
    model = Comments
    fields= ("__all__")