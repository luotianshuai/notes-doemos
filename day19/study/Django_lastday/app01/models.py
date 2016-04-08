#/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import unicode_literals
# Create your models here.

from django.db import models

class UserType(models.Model):
    typelist = models.CharField(max_length=64,null=True,blank=True)

class UserGroup(models.Model):
    caption = models.CharField(max_length=64)
    user_type = models.ForeignKey('UserType')

    def __unicode__(self):
        return self.caption

class Host(models.Model):
    hostname = models.CharField(max_length=64)
    ip = models.CharField(max_length=64)
    user_group = models.ForeignKey('UserGroup')

    def __unicode__(self):
        return self.hostname






class UserInfo(models.Model):
    username = models.CharField(max_length=64)