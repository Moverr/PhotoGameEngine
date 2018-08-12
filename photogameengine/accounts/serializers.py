import base64
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.
"""
This 
"""
user = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        label="Email Address"
    )

    username = serializers.CharField(
        required=True,
        label="Username"
    )

    password = serializers.CharField(
        required=True,
        label="Password",
        style={'input_type':'password'}
        )
    password_2 = serializers.CharField(
        required=True,
        label="Password",
        style={'input_type':'password'}
        )

    class Meta:
        model = User
        fields = ('username','email','password','password_2')
  