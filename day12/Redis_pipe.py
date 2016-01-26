#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import redis

pool = redis.ConnectionPool(host='192.168.17.15',port='6379')
r = redis.Redis(connection_pool=pool)
pipe = r.pipeline(transaction=True)
r.set('name','luotianshuai')
r.set('age',18)
pipe.execute()
