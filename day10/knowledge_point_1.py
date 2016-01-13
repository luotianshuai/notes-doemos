#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'

import Queue
obj = object() #object也是一个类，我创建了一个对象obj

q = Queue.Queue()
for i in range(10):
    print id(obj)#看萝卜号
    q.put(obj)
'''
这个队列里有10个萝卜(萝卜=obj),但是这10个萝卜只是个投影。
我们在for循环的时候put到队列里，obj有变化吗？是否有新开辟空间？显然没有
'''