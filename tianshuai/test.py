#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'

'''
def add_end(args):
    print args
print add_end('shuaige')
'''
'''
shuaige   === print args
None  == print add_end('shuaige')

因为函数没有返回值当你去print的时候为空所以这个时候获取结果的时候直接调用函数即可
add_end('shuaige') #这样就能获取到结果
'''
def add_end(args):
    a = 1
    b = 2
add_end('shuaige')


