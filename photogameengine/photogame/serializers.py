from  photogame.models import Picture,votes
from rest_framework import serializers


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Picture
        fields = ('id','file','caption' ,'description','category','owner','datecreated')
    


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = votes
        fields = ('id', 'picture','voter','count','status')