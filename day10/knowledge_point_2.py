#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import contextlib
import threading
import time
import random

doing = []
def number(l2):
    while True:
        print len(l2)
        time.sleep(1)

t = threading.Thread(target=number,args=(doing,))  #开启一个线程，每一秒打印列表，当前工作中的线程数量
t.start()


#添加管理上下文的装饰器
@contextlib.contextmanager
def show(li,iterm):
    li.append(iterm)
    yield
    '''
    yield冻结这次操作，就出去了，with就会捕捉到，然后就会执行with下的代码块，当with下的代码块
    执行完毕后就会回来继续执行yield下面没有执行的代码块！
    然后就执行完毕了
    如果with代码块中的非常耗时，那么doing的长度是不是一直是1，说明他没执行完呢？我们就可以获取到正在执行的数量，当他with执行完毕后
    执行yield的后续的代码块。把他移除后就为0了！
    '''
    li.remove(iterm)




def task(arg):
    with show(doing,1):#通过with管理上下文进行切换
        print len(doing)
        time.sleep(10) #等待10秒这里可以使用random模块来操作~

for i in range(20): #开启20个线程执行
    temp = threading.Thread(target=task,args=(i,))
    temp.start()

'''
作用：我们要记录正在工作的的列表
比如正在工作的线程我把加入到doing这个列表中，如果工作完成的把它从doing列表中移除。
通过这个机制，就可以获取现在正在执行的线程都有多少
'''