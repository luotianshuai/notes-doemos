#/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserType(models.Model):
    caption = models.CharField(max_length=32)

class UserInfo(models.Model):
    user_type = models.ForeignKey('UserType') #这个user_type是一个对象,对象里面封装了ID和caption
    username = models.CharField(max_length=32)
    age = models.IntegerField()

#点赞实例
#用户表
class MyUser(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    def __unicode__(self):
        return self.username

#新闻表
class News(models.Model):
    #标题
    title = models.CharField(max_length=32)
    #内容
    content = models.CharField(max_length=256)
    def __unicode__(self):
        return self.title

#点赞表
class Favor(models.Model):
    '''
    这里需要注意,首先这个赞是谁点的,并且谁给某个新闻点的赞!
    如果你点过就不能再点了
    '''
    user_obj = models.ForeignKey('MyUser')
    news_obj = models.ForeignKey('News')
    def __unicode__(self):
        return '用户:%s ---->赞文章:%s' % (self.user_obj.username,self.news_obj.title)




########################多对多#########################


class Host(models.Model):
    hostname = models.CharField(max_length=32)
    port = models.IntegerField()

class HostAdmin(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    host = models.ManyToManyField('Host')

########################自定义多对多####################




class HostInfo(models.Model):
    hostname = models.CharField(max_length=32)
    port = models.IntegerField()

class UserMap(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

    #through告诉Django用那张表做关联
    host = models.ManyToManyField(HostInfo , through='HostRelation')

class HostRelation(models.Model):
    host = models.ForeignKey('HostInfo')
    user = models.ForeignKey('UserMap')

    '''
    并且这里我们可以添加多个关系,比如在加一个字段
    usertype = models.ForeignKey('UserType')
    或者增加一个普通字段
    status = models.CharField(max_length=32)
    '''



