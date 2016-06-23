#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'



from multiprocessing import Pool
class a(object):
    def run(self):
        return '1'
x = a()
pool = Pool(1)


for i in range(0,4):
    pool.apply_async(x.run,())
pool.close()
pool.join()