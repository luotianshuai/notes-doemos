#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import random
import time


def handler(array):
    for i in range(len(array)):
        smallest_index = i  #假设默认第一个值最小
        for j in range(i,len(array)):
            if array[smallest_index] > array[j]:
                smallest_index = j  #如果找到更小的,记录更小元素的下标
        '''
        小的循环结束后在交换,这样整个小循环就之前的的选择排序来说,少了很多的替换过程,就只替换了一次!提升了速度
        '''
        tmp = array[i]
        array[i] = array[smallest_index]
        array[smallest_index] = tmp


if __name__ == '__main__':
    array = []
    old_time = time.time()
    for i in range(50000):
        array.append(random.randrange(1000000))
    handler(array)
    print(array)
    print('Cost time is :',time.time() - old_time)
