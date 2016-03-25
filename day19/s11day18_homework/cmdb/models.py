#/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


#这个类是用来生成数据库表的,这个类必须集成models.Model
class UserInfo(models.Model):
    username = models.CharField(max_length=64) #这个就表示去数据库创建一个字符串类型的字段
    password = models.CharField(max_length=64)#对于字符串类型的字段必须设置一个最大长度
    group = models.ForeignKey('Gorup') #数组外键关联
    def __unicode__(self):
        return self.username

class HostInfo(models.Model):
    hostname = models.CharField(max_length=64)
    hostip = models.CharField(max_length=64)
    hostport = models.CharField(max_length=64)
    hoststatus = models.ForeignKey('HostStatus') #状态外键关联
    hostbusiness = models.ForeignKey('HostBusiness') #业务线外键关联
    group = models.ForeignKey('Gorup') #主机数组关联
    def __unicode__(self):
        return self.hostname

class Gorup(models.Model):
    groupname = models.CharField(max_length=64)
    def __unicode__(self):
        return self.groupname

class HostStatus(models.Model):
    hoststatus = models.CharField(max_length=64)
    def __unicode__(self):
        return self.hoststatus

class HostBusiness(models.Model):
    hostbusiness = models.CharField(max_length=64)
    def __unicode__(self):
        return self.hostbusiness