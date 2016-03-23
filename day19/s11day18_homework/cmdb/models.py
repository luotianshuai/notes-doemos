#/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


#这个类是用来生成数据库表的,这个类必须集成models.Model
class UserInfo(models.Model):
    #创建表的字段
    email = models.CharField(max_length=64) #这个就表示去数据库创建一个字符串类型的字段
    passwords = models.CharField(max_length=64)#对于字符串类型的字段必须设置一个最大长度

class HostInfo(models.Model):
    #创建表的字段
    #host_id = models.CharField(max_length=32)
    host_name = models.CharField(max_length=64)
    host_port = models.CharField(max_length=64)
    host_ip = models.CharField(max_length=64)
    host_business = models.CharField(max_length=64)
    host_status = models.CharField(max_length=64)
    host_id = models.CharField(max_length=64)



