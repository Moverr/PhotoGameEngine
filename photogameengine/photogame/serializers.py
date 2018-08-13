from  photogame.models import Picture,Votes,Views
from rest_framework import serializers


class PictureSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Picture
        fields = ('id','file','caption' ,'description','category','owner','datecreated')
    

class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Votes
        fields = ('id', 'picture','voter','count','status','datecreated')

class ViewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Views
        fields = ('id', 'picture','voter','count','datecreated')

 