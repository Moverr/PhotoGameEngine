import base64
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import UserProfile

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

    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email Already Exists")

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(" Username Already Exists")
        return value

    def validate_password(self, value):
        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 6):
            raise serializers.ValidationError(
                "Password should be atleast %s characters long." % getattr(settings, 'PASSWORD_MIN_LENGTH', 6)
            )
        return value
    
    def validate_password_2(self, value):
        data = self.get_initial()
        password = data.get('password')
        if password != value:
            raise serializers.ValidationError("Passwords doesn't match.")
        return value
    
    def create(self, validated_data):
        user_data = {
            'username': validated_data.get('username'),
            'email': validated_data.get('email'),
            'password': validated_data.get('password')           
        }
        is_active = True
        user = UserProfile.objects.create_user_profile(
                data=user_data,
                is_active=is_active,
                site=get_current_site(self.context['request']),
                send_email=True
            )
        return validated_data