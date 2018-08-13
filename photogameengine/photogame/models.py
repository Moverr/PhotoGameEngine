import datetime
from datetime import datetime
from enum import Enum
 
from django.db import models

 
VOTE_CHOICE = (
    (1,"UPVOTE"),
    (2,"DOWNVOTE"), 
    )

PHOTO_CATEGORY = (
    ("PEOPLE", "People"),
    ("NATURE", "Nature"),
    ("CITYLIFE", "City Life"),
    ("LOVE", "Love"),
    ("SPORTS", "Sports"),
    ("FAMILY", "Family"),
    )

class Picture(models.Model): 
    file = models.FileField(blank=False, null=True)   
    url = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    description = models.TextField('description')
    category = models.CharField(choices=PHOTO_CATEGORY, max_length=100)
    owner = models.ForeignKey('auth.User',related_name='pictures',on_delete=models.CASCADE)
    datecreated = models.DateTimeField(auto_now_add=True,blank=True)

class PictureVotes(models.Model):
    picture = models.ForeignKey(Picture,on_delete=models.CASCADE)
    voter = models.ForeignKey('auth.User',related_name='voters',on_delete=models.CASCADE)
    count = models.IntegerField()   
    status = models.CharField(choices=VOTE_CHOICE, max_length=100)
    datecreated = models.DateTimeField(auto_now_add=True,blank=True)

class PictureViews(models.Model):
    picture = models.ForeignKey(Picture,on_delete=models.CASCADE)
    viewer = models.ForeignKey('auth.User',related_name='viewer',on_delete=models.CASCADE)
    count = models.IntegerField()   
    datecreated = models.DateTimeField(auto_now_add=True,blank=True)
    
    


