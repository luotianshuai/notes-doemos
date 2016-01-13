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

        self.q = Queue(0)
        self.max = maxthreads
        self.name = name
        self.waiters = []
        self.working = []

    def start(self):
        needsiZe = self.q.qsize()
        while self.workers < min(self.max, needSize):
            self.startAWorker()

    def startAWorker(self):
        self.workers += 1
        name = "PoolThread-%s-%s" % (self.name or id(self), self.workers)
        newThread = self.threadFactory(target=self._worker, name=name)
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
        o = self.q.get()
        while o is not WorkerStop:
            with self._workerState(self.working, ct):
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

            with self._workerState(self.waiters, ct):
                o = self.q.get()

    def stop(self):
        while self.workers:
            self.q.put(WorkerStop)
            self.workers -= 1


def show(arg):
    import time
    time.sleep(1)
    print arg


pool = ThreadPool(20)

for i in range(500):
    pool.callInThread(show, i)

pool.start()
pool.stop()