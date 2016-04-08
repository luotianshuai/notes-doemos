#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'
import redis

ClientIP = '192.168.17.15'

RedisServer = '127.0.0.1'
RedisPort = 6379
RedisSubChannel = 'fm100'
RedisPubChannel = 'fm101'


#
# if __name__ == '__main__':
#     r = redis.Redis(host='127.0.0.1',port=6379)
#     r.set('name','shuaige')
#     ret = r.get('name')
#     print ret