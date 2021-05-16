from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', "first_name", "last_name", "profile_image")