import datetime
from datetime import datetime
from enum import Enum

from django.db import models

from photogame.utils.enums import Categories,VoteStatus


# Create your models here.
class Picture(models.Model): 
    file = models.FileField(blank=False, null=True)   
    url = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    description = models.TextField('description')
    category = models.CharField(max_length=255, choices=[ (tag,tag.value) for tag in Categories] )
    owner = models.ForeignKey('auth.User',related_name='pictures',on_delete=models.CASCADE)
    datecreated = models.DateTimeField(auto_now_add=True,blank=True)

class votes(models.Model):
    picture = models.ForeignKey(Picture,on_delete=models.CASCADE)
    voter = models.ForeignKey('auth.User',related_name='voters',on_delete=models.CASCADE)
    count = models.IntegerField()
    status = models.CharField(max_length=255, choices=[ (tag,tag.value) for tag in VoteStatus] )


