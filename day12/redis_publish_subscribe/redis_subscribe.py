#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

from redis_helper import RedisHelper

obj = RedisHelper() #实例化对象
redis_sub = obj.subscribe()#调用订阅方法

while True:
    msg = redis_sub.parse_response()#接收发布消息
    print msg
