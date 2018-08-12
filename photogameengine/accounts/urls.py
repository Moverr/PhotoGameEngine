from  django.conf.urls import  url
from . import views
from django.urls import path
from rest_framework import routers
# from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
     url(r'^$',views.UserRegistration.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)