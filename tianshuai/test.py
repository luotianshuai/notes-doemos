#/usr/bin/env python
#-*- coding:utf-8 -*-

import memcache

mc = memcache.Client(['127.0.0.1:11211'],debug=True)
mc.set('name','luotianshuai',60)
mc.set('age','8',60)
mc.set('shuaige','luotianshuai',60)