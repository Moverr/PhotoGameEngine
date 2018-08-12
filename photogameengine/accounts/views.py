from django.shortcuts import render
from rest_framework.views import APIView
from django.http import request
from accounts.serializers import UserRegistrationSerializer

# Create your views here.
class UserRegistration(APIView):
    # todo : register new User
    def post(self,request,format=None):
        serializer = 