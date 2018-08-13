from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from photogame.models import Picture,PictureVotes,PictureViews

from .serializers import PictureSerializer, VoteSerializer,ViewsSerializer
from rest_framework.views import APIView
 

class PictureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that manages picture information 
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PictureVoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint  that manages picture voting 
    """
    queryset = PictureVotes.objects.all()
    serializer_class = VoteSerializer


class PictureViewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint  that manages picture views .
    """
    queryset = PictureViews.objects.all()
    serializer_class = ViewsSerializer

