#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'


from redis_helper import RedisHelper
obj = RedisHelper() #实例化方法
obj.publish('hello') #执行发布


