from rest_framework import serializers
from .models import Books, Authors, Chapters, BookComments, Expand, Timeline, Characters


class AuthorsSerializers(serializers.ModelSerializer):
  class Meta:
    model = Authors
    fields = "__all__"


class BooksSerializers(serializers.ModelSerializer):
  authors = AuthorsSerializers(many=True)

  class Meta:
    model = Books
    fields = "__all__"


class ChaptersSerializers(serializers.ModelSerializer):
  class Meta:
    model = Chapters
    fields = "__all__"


class ExpandSerializers(serializers.ModelSerializer):
  class Meta:
    model = Expand
    fields = "__all__"


class CommentCommentsSerializers(serializers.ModelSerializer):
  class Meta:
    model = BookComments
    fields = "__all__"


class BookCommentsSerializers(serializers.ModelSerializer):
  comment_comment = CommentCommentsSerializers()

  class Meta:
    model = BookComments
    fields = "__all__"

class TimelineSerializers(serializers.ModelSerializer):

  class Meta:
    model = Timeline
    fields = "__all__"

class CharactersSerializers(serializers.ModelSerializer):

  class Meta:
    model = Characters
    fields = "__all__"
