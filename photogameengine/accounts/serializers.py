import base64
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import UserRegistrationModel



# Create your views here.
"""
This 
"""
user = get_user_model()
user_registration = UserRegistrationModel()

class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
  
    def create(self,validate_data):
        return User.objects.create(**validate_data)

    class Meta:
        model = User
        fields = ['username','email','password']
