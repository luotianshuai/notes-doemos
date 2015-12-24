#/usr/bin/env python
#-*- coding:utf-8 -*-

import sys,time
from progressbar import *
total = 1000
 
#基本用法

progress = ProgressBar()
for i in progress(range(total)):
 time.sleep(0.01)

'''
pbar = ProgressBar().start()
for i in range(1,1000):
  pbar.update(int((i/(total-1))*100))
  time.sleep(0.01)
pbar.finish()
'''
'''
this function must install :progressbar

1.
if you system is windows you should be install pip

windows install pip
http://www.tuicool.com/articles/eiM3Er3

will pip install done install pip
pip install progressbar

2.
if you system is linux

yum -y install pip
pip install progressbar

'''

'''
#高级用法
widgets = ['Progress: ', Percentage(), ' ', Bar(marker=RotatingMarker('>-=')),
      ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
for i in range(1000000):
 # do something
 pbar.update(10*i+1)
 time.sleep(0.0001)
pbar.finish()
'''
