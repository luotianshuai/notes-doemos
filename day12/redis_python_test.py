#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import redis
'''
r = redis.Redis(host='192.168.17.15',port=6379) #设置连接的主机和端口
r.set('name','luotianshuai')#添加一条记录
print r.get('name')#获取一条记录

r =redis.StrictRedis

'''
'''
#连接池
rpool = redis.ConnectionPool(host='192.168.17.15',port=6379) #创建连接池连接对象

r = redis.Redis(connection_pool=rpool)#把创建的对象赋值给connection_pool
r.set('username','luotianshuai') #添加一条记录
print r.get('username')#获取一条记录
'''
rpool = redis.ConnectionPool(host='192.168.17.15',port=6379) #创建连接池连接对象
r = redis.Redis(connection_pool=rpool)#把创建的对象赋值给connection_pool
pipe = r.pipeline(transaction=True) #启用事物处理
r.set('name','luotianshuai')
r.set('age','18')
pipe.execute()
print r.get('name'),r.get('age')
