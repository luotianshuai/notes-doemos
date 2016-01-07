#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time
  
def show(arg):
    time.sleep(2)
    print 'thread'+str(arg)
  
for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()
  
print 'main thread stop'