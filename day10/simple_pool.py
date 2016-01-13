#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import Queue
import threading
import time

'''
这个简单的例子的想法是通过：
1、利用Queue特性，在Queue里创建多个线程对象
2、那我执行代码的时候，去queue里去拿线程！
如果线程池里有可用的，直接拿。
如果线程池里没有可用，那就等。
3、线程执行完毕，归还给线程池
'''

class ThreadPool(object): #创建线程池类
    def __init__(self,max_thread=20):#构造方法，设置最大的线程数为20
        self.queue = Queue.Queue(max_thread) #创建一个队列
        for i in xrange(max_thread):#循环把线程对象加入到队列中
            self.queue.put(threading.Thread)
            #把线程的类名放进去，执行完这个Queue

    def get_thread(self):#定义方法从队列里获取线程
        return self.queue.get()

    def add_thread(self):#定义方法在队列里添加线程
        self.queue.put(threading.Thread)

pool = ThreadPool(10)

def func(arg,p):
    print arg
    time.sleep(2)
    p.add_thread() #当前线程执行完了，我在队列里加一个线程！

for i in xrange(300):
    thread = pool.get_thread() #线程池10个线程，每一次循环拿走一个！默认queue.get()，如果队列里没有数据就会等待。
    t = thread(target=func,args=(i,pool))
    t.start()


'''
self.queue.put(threading.Thread) 添加的是类不是对象，在内存中如果相同的类只占一份内存空间
并且如果这里存储的是对象的话每次都的新增都得在内存中开辟一段内存空间

还有如果是对象的话：下面的这个语句就不能这么调用了！
for i in xrange(300):
    thread = pool.get_thread()
    t = thread(target=func,args=(i,pool))
    t.start()
    通过查看源码可以知道，在thread的构造函数中：self.__args = args  self.__target = target  都是私有字段那么调用就应该这么写

for i in xrange(300):
    ret = pool.get_thread()
    ret._Thread__target = func
    ret._Thread__args = (i,pool)
    ret.start()
'''