from django.shortcuts import render
from rest_framework.views import APIView
from django.http import request
from django.http import request
from django.http.response import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


from accounts.serializers import UserRegistrationSerializer
from .models import UserRegistrationModel

# Create your views here.
permission_classes = (permissions.AllowAny,)
class UserRegistration(APIView):
    # todo : register new User
    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class UserLogin(APIView):
#     def post(self,request,format=None):
        
        
