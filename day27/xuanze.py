#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'
import random
import time
#maopao_list = [69, 471, 106, 66, 149, 983, 160, 57, 792, 489, 764, 589, 909, 535, 972, 188, 866, 56, 243, 619]

def handler(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] > array[j]:
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp



if __name__ == '__main__':
    array = []
    old_time = time.time()
    for i in range(50000):
        array.append(random.randrange(1000000))
    handler(array)
    print array
    print 'Cost time is :',time.time() - old_time
