#!/usr/bin/env python
#-*- coding:utf-8 -*-

import memcache

mc = memcache.Client(['192.168.17.15:11211'],debug=True)
while True:
    user_input = raw_input('\033[34;1mPlease input ke:value like username:luotianshuai \n==>:\33[0m')
    user_inputk = user_input.split(':')[0]
    user_inputv = user_input.split(':')[1]
    mc.set(user_inputk,user_inputv)
    result = mc.get(user_inputk)
    print '\033[32;1mYou\'re input is %s\033[0m' % user_inputv

