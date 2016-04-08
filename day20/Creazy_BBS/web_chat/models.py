#/usr/bin/env python
#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from web.models import UserProfile

# Create your models here.

class QQGroup(models.Model):
    '''
    QQ组表
    '''
    #组名
    name = models.CharField(max_length=64,unique=True)
    #注释
    description = models.CharField(max_length=255,default="The Admin is so lazy,The Noting to show you ....")

    '''
    线面members和admins在做跨表关联的时候,关联的表不能使用双引号!
    '''
    #成员
    members = models.ManyToManyField(UserProfile,blank=True)
    #管理员
    admins = models.ManyToManyField(UserProfile,blank=True,related_name='group_admins')
    '''
    如果在一张表中,同样调用了另一张表同样的加related_name
    '''
    #最大成员数量
    max_member_nums = models.IntegerField(default=200)
    def __unicode__(self):
        return self.name