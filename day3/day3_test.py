#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info = raw_input('\033[33;1mplease input your backen\033[0m')\
'''
info = 'www.oldboy.org'

with open('haproxy.conf','r') as f:
    for index in range(len(f.readlines())):
        line = f.next()
        print line
        '''
# Open a file
'''
fo = open("haproxy.conf", "r")
print "Name of the file: ", fo.name

for index in range(int(len(fo.readline()))):
   line = fo.next()
   print "Line No %d - %s" % (index, line)
   '''
fo = open("haproxy.conf", "r")
print int(len(fo.readlines()))
