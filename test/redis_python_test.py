#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import redis

r = redis.Redis(host='192.168.17.15',port=6379) #设置连接的主机和端口
r.set('name','luotianshuai')#添加一条记录
print r.get('name')#获取一条记录

r =redis.StrictRedis

