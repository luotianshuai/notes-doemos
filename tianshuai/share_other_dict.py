#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'

l1=['a','b']
l2=[1,2]
l3=[4,5]
#方式1
#dic = {'a':{1:4},'b':{2:{5}}}
'''
dic = {}
for i in l1:
    dic[i] = {l2[l1.index(i)]:l3[l1.index(i)]}
print dic
'''

#方式2

#print dict(map(lambda a1,a2,a3:(a1,{a2:a3}),l1,l2,l3))
#print dict(map(lambda a1,a2,a3:(a1,{a2:a3}),l1,l2,l3))
print zip(l1,l2)
print dict(zip(l1,l2))



e = {"hello":1,"python":2,"shuaige":3,"meinv":4}
print ":".join(e)
