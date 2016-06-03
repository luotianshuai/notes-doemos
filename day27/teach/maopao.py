#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'
import random

maopao_list = [69, 471, 106, 66, 149, 983, 160, 57, 792, 489, 764, 589, 909, 535, 972, 188, 866, 56, 243, 619]


def handler(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp



if __name__ == '__main__':
    handler(maopao_list)
    print(maopao_list)


'''
array = []
for i in range(50000):
    array.append(random.randrange(100000000))
print(array)
'''