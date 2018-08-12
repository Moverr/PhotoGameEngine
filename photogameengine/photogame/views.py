from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from photogame.models import Picture, votes

from .serializers import PictureSerializer, VoteSerializer
from rest_framework.views import APIView


# class PictureViewSet(APIView):   
#     def get(self,request,format=None):
#         pictures = Picture.objects.all()
#         serializer = PictureSerializer(pictures)
#         return Response(serializer.data)
    
       
# class VoteViewSet(APIView):
#     def get(self,request,format=None):
#         pictures = votes.objects.all()
#         serializer = VoteSerializer(pictures)
#         return Response(serializer.data)   
     



class PictureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class VoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = votes.objects.all()
    serializer_class = VoteSerializer

