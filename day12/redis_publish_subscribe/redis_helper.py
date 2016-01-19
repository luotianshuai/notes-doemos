#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import redis

class RedisHelper(object):
    def __init__(self):#构造方法
        self.__conn = redis.Redis(host='192.168.17.15',port=6379)#连接Redis
        self.channel = 'monitoring' #定义channel名称

    def publish(self,msg):#定义发布方法
        self.__conn.publish(self.channel,msg)
        return True

    def subscribe(self):#定义订阅方法
        pub = self.__conn.pubsub()#连接channel
        pub.subscribe(self.channel)#订阅channel
        pub.parse_response()
        return pub

