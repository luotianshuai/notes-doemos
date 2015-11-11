#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info = raw_input('\033[33;1mplease input your backen\033[0m')
info = 'www.oldboy.org'
with open('haproxy.conf','r') as f:
    for k,v in enumerate(f.readlines()):
        v = v.strip()
        #print k,v
        if info in v and v[0:6] == 'backen':
            print next(v)
