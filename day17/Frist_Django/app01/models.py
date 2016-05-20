#/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


#这个类是用来生成数据库表的,这个类必须集成models.Model
class UserInfo(models.Model):
    #创建表的字段
    email = models.CharField(max_length=16) #这个就表示去数据库创建一个字符串类型的字段
    pwd = models.CharField(max_length=32)#对于字符串类型的字段必须设置一个最大长度
    #
