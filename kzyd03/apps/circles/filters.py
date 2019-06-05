import django_filters
from django.db.models import Q
from .models import Circles, Comments


class CirclesFilter(django_filters.rest_framework.FilterSet):
  """
  获取用户畅想圈
  """

  class Meta:
    model = Circles
    fields = ['sub_man', 'circle_id']

class CircleCommentFilter(django_filters.rest_framework.FilterSet):
  """
  获取用户的评论
  """

  class Meta:
    model = Comments
    fields = ['sub_man', 'comment_chapter']
