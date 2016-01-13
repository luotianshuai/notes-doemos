#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
from Queue import Queue
import contextlib
import threading

WorkerStop = object()


class ThreadPool:
    workers = 0
    threadFactory = threading.Thread
    currentThread = staticmethod(threading.currentThread)

    def __init__(self, maxthreads=20, name=None):
        self.q = Queue(0) #这里创建一个队列，如果是0的话表示不限制，现在这个队列里放的是任务
        self.max = maxthreads #定义最大线程数
        self.name = name
        self.waiters = []#这两个是用来计数的
        self.working = []#这两个是用来技术的

    def start(self):
        #self.max 最大线程数
        #q.qisze()，任务个数
        needSize = self.q.qsize()
        while self.workers < min(self.max, needSize):#min(10,20)取最小值
            #wokers默认为0  【workers = 0】
            '''
            举例来说：
            while self.workers < min(self.max, needSize):
            这个循环，比如最大线程为20，咱们的任务个数为10，取最小值为10
            每次循环开1个线程，并且workers自增1，那么循环10次后，开了10个线程了workers = 10 ,那么workers就不小于10了
            就不开线程了，我线程开到最大了，你们这10个线程去消耗这10个任务去吧
            并且这里不阻塞，创建完线程就去执行了！
            每一个线程都去执行_worker方法去了
            '''
            self.startAWorker()

    def startAWorker(self):
        self.workers += 1
        newThread = self.threadFactory(target=self._worker, name='shuaige') #创建一个线程并去执行_worker方法
        newThread.start()

    def callInThread(self, func, *args, **kw):
        self.callInThreadWithCallback(None, func, *args, **kw)

    def callInThreadWithCallback(self, onResult, func, *args, **kw):
        o = (func, args, kw, onResult)
        self.q.put(o)


    @contextlib.contextmanager
    def _workerState(self, stateList, workerThread):
        stateList.append(workerThread)
        try:
            yield
        finally:
            stateList.remove(workerThread)

    def _worker(self):
        ct = self.currentThread()
        o = self.q.get() #去队列里取任务,如果有任务就O就会有值，每个任务是个元组，有方法，有参数
        while o is not WorkerStop:
            with self._workerState(self.working, ct):  #上下文切换
                function, args, kwargs, onResult = o
                del o
                try:
                    result = function(*args, **kwargs)
                    success = True
                except:
                    success = False
                    if onResult is None:
                        pass
                    else:
                        pass

                del function, args, kwargs

                if onResult is not None:
                    try:
                        onResult(success, result)
                    except:
                        #context.call(ctx, log.err)
                        pass

                del onResult, result

            with self._workerState(self.waiters, ct): #当线程工作完闲暇的时候，在去取任务执行
                o = self.q.get()

    def stop(self): #定义关闭线程方法
        while self.workers: #循环workers值
            self.q.put(WorkerStop) #在队列中增加一个信号~
            self.workers -= 1 #workers值-1 直到所有线程关闭


def show(arg):
    import time
    time.sleep(1)
    print arg


pool = ThreadPool(10)

#创建500个任务，队列里添加了500个任务
#每个任务都是一个元组（方法名，动态参数，动态参数，默认为NoNe）
for i in range(100):
    pool.callInThread(show, i)

pool.start()  #队列添加完成之后，开启线程让线程一个一个去队列里去拿

pool.stop() #当上面的任务都执行完之后，线程中都在等待着在队列里去数据呢！
'''
我们要关闭所有的线程，执行stop方法，首先workers这个值是当前的线程数量，我们给线程发送一个信号“WorkerStop”
在线程的工作里：        while o is not WorkerStop:   如果线程获取到这个值就不执行了，然后这个线程while循环就停止了，等待
python的垃圾回收机制，回收。

然后在self.workers -= 1 ，那么所有的线程收到这个信号之后就会停止！！！
over~
'''