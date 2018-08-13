from  photogame.models import Picture,PictureVotes,PictureViews
from rest_framework import serializers


class PictureSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Picture
        fields = ('id','file','caption' ,'description','category','owner','datecreated')
    

class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PictureVotes
        fields = ('id', 'picture','voter','count','status','datecreated')

class ViewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PictureViews
        fields = ('id', 'picture','viewer','count','datecreated')

 