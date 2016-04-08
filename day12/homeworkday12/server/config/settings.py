#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'
import redis

RedisServer = '127.0.0.1'
RedisPort = 6379
RedisSubChannel = 'fm101'
RedisPubChannel = 'fm100'


#
# if __name__ == '__main__':
#     r = redis.Redis(host='127.0.0.1',port=6379)
#     r.set('name','shuaige')
#     ret = r.get('name')
#     print ret