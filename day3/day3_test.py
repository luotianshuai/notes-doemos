#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info = raw_input('\033[33;1mplease input your backen\033[0m')
info = 'www.oldboy.org'
with open('haproxy.conf','r') as f:
    for i in f.readlines():
        i = i.strip('\n')
        if info in i and i[0:6] == 'backen':
            print i