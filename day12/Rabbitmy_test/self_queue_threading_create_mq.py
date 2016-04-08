#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import Queue
import threading

messagequeue = Queue.Queue(10) #创建最多有10个元素的队列

def producer(i):#创建生产者
    while True:
        messagequeue.put(i)

def consumer(i):#创建消费者
    while True:
        messagequeue.get(i)

for i in range(5): #创建5个线程不断的生产
    t = threading.Thread(target=producer,args=(i,))
    t.start()

for i in range(2): #创建5个线程不断的消费
    t = threading.Thread(target=consumer,args=(i,))
    t.start()



