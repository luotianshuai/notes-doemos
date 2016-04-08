#!/usr/bin/env python
#coding:utf-8
   
import threading
import time
   
gl_num = 0
   
lock = threading.RLock() #实例化调用线程锁
   
def Func():
    lock.acquire() #获取线程锁
    global gl_num
    gl_num +=1
    time.sleep(1)
    print gl_num
    lock.release() #释放线程锁，这里注意，在使用线程锁的时候不能把锁，写在代码中，否则会造成阻塞，看起来“像”单线程
       
for i in range(10):
    t = threading.Thread(target=Func)
    t.start()