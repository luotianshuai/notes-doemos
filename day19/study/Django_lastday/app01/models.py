from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

class userinfo(models.Model):
    name = models.CharField(max_length=32)
    ctime = models.DateTimeField(auto_now=True)
    uptime = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=32,null=True)
    email2 = models.GenericIPAddressField(protocol="ipv4",null=True,blank=True)
    img = models.ImageField(null=True,blank=True,upload_to="upload")
    def __unicode__(self):
        return self.name




class SimpleModel(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)