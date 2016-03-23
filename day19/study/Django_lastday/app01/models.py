#/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=64,null=True)
    email2 = models.EmailField(max_length=64,default="luotianshuai@qq.com")
    ctime = models.DateTimeField(auto_now=True) #默认这样写上就不用管了,每当你创建一行数据的时候就会在那一行数据中增加一个ctime字段
    uptime = models.DateTimeField(auto_now_add=True)#默认写成这样也不同管了,当前表任何一行有修改的时候他就会自动更新.

    def __unicode__(self):
        return self.username
    #上面的__unicode__(self)方法,是当你输出这个类/或者对象的时候某人输出,比如这个输出的是这个username这一列.