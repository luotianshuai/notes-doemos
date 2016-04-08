#!/usr/bin/env  python
#-*- coding:utf-8 -*-


#1、装饰器是一个函数，至少2层

def w1(func):
    def inner(*args,**kwargs):
        print 'gongneng1'
        func(*args,**kwargs)
        print 'gongneng2'
    return inner
def w2(func):
    def inner(*args,**kwargs):
        print 'gongneng3'
        func(*args,**kwargs)
        print 'gongneng4'
    return inner

@w1
@w2
def f1(arg,arg2,arg3):
    print arg,arg2,arg3

f1('nihao','tianshuai','shuaige')