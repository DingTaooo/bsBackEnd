from rest_framework import serializers
from .models import UserProfile
from rest_framework import status


class UsersSerializers(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields= ('name', 'user_image')