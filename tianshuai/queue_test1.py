#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import Queue
'''
import Queue

q = Queue.Queue() #调用队列生成对象
q.put(1)  #存放第一个值到队列
q.put(2)  #存放第二个值到队列


print 'get frist one:',q.get() #获取队列的第一个值
print 'get second on:',q.get() #获取队列的第二个值
'''

q = Queue.Queue() #调用队列生成对象
try:
    q.get_nowait()
except Queue.Empty as f:
    print 'The Queue is empty!'

