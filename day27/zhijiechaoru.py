#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'


import random
import time
#maopao_list = [69, 471, 106, 66, 149, 983, 160, 57, 792, 489, 764, 589, 909, 535, 972, 188, 866, 56, 243, 619]

def handler(array):
    for i in range(1,len(array)):
        position = i #刚开始往左边走的第一个位置
        current_val = array[i] #先把当前值存下来
        while position > 0 and current_val < array[position -1]:
            array[position] = array[position - 1] #如果条件成立把当前的值替换为他上一个值
            position -= 1
        #当上面的条件都不成立的时候{左边没有值/左边的值不比自己的值小}
        array[position] = current_val  #把值替换






if __name__ == '__main__':
    array = []#[69, 471, 106, 66, 149, 983, 160, 57, 792, 489, 764, 589, 909, 535, 972, 188, 866, 56, 243, 619]
    old_time = time.time()
    for i in range(50000):
        array.append(random.randrange(1000000))
    handler(array)
    print array
    print 'Cost time is :',time.time() - old_time
