#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import os
import sys
import redis


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取文件所在的顶级目录，方便加载其他的模块
sys.path.append(BASE_DIR) #加载环境变量

from config import settings #导入config模块，把配置导入到Redis连接配置中，下面的class RedisHelper：代码中

class RedisHelper(object):
    def __init__(self):
        self.__conn = redis.Redis(host=settings.RedisServer,port=settings.RedisPort) #连接Redis
        self.sub = settings.RedisSubChannel #设置sub通道
        self.pub = settings.RedisPubChannel #设置pub通道

    def set(self,key,values): #定义设置方法
        self.__conn.set(key,values)

    def get(self,key):#定义查询方法
        return self.__conn.get(key)

    def keys(self,pattern="*"):#定义查询所有keys方法
        return self.keys(pattern)

    def subscribe(self):
        pub = self.__conn.publish()
        pub.subscribe(self.sub)
        pub.parse_response()
        return pub
