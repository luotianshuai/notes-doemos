#!/usr/bin/env python
#-*-  coding:utf-8 -*-

import threading
import time

def show(arg):
    print 'start',arg
    print arg/2
    time.sleep(arg/2)
    print 'stop',arg
tl = []


for i in range(10):
    t = threading.Thread(target=show, args=(i*4,))
    tl.append(t)
    t.start()

while tl:
    t = tl.pop()
    #t.join()
    print tl

print 'tl : ',tl
print 'main thread stop'