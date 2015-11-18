#!/usr/bin/env  python
#-*- coding:utf-8 -*-
import time

###########################################例子1##############################################################
'''
def say():
    print 'I am saying the words'

#需求：
#    首先我要给say这个函数添加一个输出消耗时间！

#解决方法：
#    把逻辑进行封装了，但是调用的时候的使用 decorator去调用需求是实现了，他并是不完美的！
def decorator(func):
    start = time.clock()
    func()
    end = time.clock()
    print "Time:%f" % (end - start)

decorator(say)   #这里在调用的时候的使用decorator()
'''
'''
输出结果：
I am saying the words
Time:0.000012
'''

#注：上面的函数仅仅把逻辑进行封装了，调用的方式也改变了，如果休要变更的代码量比较大，重复修改调用方式
#也是很难受的！看下面的装饰器！

###########################################例子2##############################################################
'''
def say():
    print 'I am saying the words'

def decorator(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print "Time:%f" % (end - start)
    return wrapper

say = decorator(say)
say()
'''
'''
输出结果：
I am saying the words
Time:0.000018
'''
#我在装饰器的基础上在给他加一层装饰器，decorator调用say函数的时候，wrapper函数里把逻辑进行封装了，然后返回出一个函数！
#然后在调用的时候就不用修改他的调用方式了直接使用：say()


###########################################例子3##############################################################
'''
#我又有新功能了，我要在上面输出开始结尾上，在加一个开始和结束
#在上一次功能上在次封装一下！


def say():
    print 'I am saying the words'

def decorator(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print "Time:%f" % (end - start)
    return wrapper

def output_log(func):
    def wrapper():
        print "start %s" % (func)
        func()
        print "end %s" % (func)
    return wrapper

say = decorator(say)
say = output_log(say)


say()

say = decorator(say)
'''

'''
输出结果：
start <function wrapper at 0x0000000002799BA8>
I am saying the words
Time:0.000004
end <function wrapper at 0x0000000002799BA8>
'''

#装饰器就是设计模式

#实例
def decorator(func):
    def wrapper(*args,**kargs):
        print "start...."
        start = time.clock()
        func(*args,**kargs)
        end = time.clock()
        print "Time: %f" % (end - start)
        print "end......"
    return wrapper

@decorator
def count(a,b):
    print a + b
@decorator
def times(a,b):
    print a * b
@decorator
def say():
    print "I am saying the words"


count(9,10)
times(9,100)
say()

#我新功能也加了但是函数的调用没有变！
'''
输出结果：
start....
19
Time: 0.000006
end......
start....
900
Time: 0.000005
end......
start....
I am saying the words
Time: 0.000004
end......
'''