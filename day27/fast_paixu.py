#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:luotianshuai
import random
import time

def quick_sort(array,start,end):
    if start >= end:
        return
    k = array[start]
    left_flag = start
    right_flag = end
    while left_flag < right_flag:
        '''
        left_flag = start 默认为0
        right_flag = end 默认为穿过来的列表总长度
        当left_flag 小与right_flag的时候成立,说明左右两边的小旗子还没有集合(为相同的值)
        '''

        #右边旗子
        while left_flag < right_flag and array[right_flag] > k:#代表要继续往左一移动小旗子
            right_flag -= 1
        '''
        如果上面的循环停止说明找到右边比左边的值小的数了,需要进行替换
        '''
        tmp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = tmp

        #左边旗子
        while left_flag < right_flag and array[left_flag] <= k:
            #如果没有找到比当前的值大的,left_flag 就+=1
            left_flag += 1
        '''
        如果上面的循环停止说明找到当前段左边比右边大的值,进行替换
        '''
        tmp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = tmp

    #进行递归把问题分半
    quick_sort(array,start,left_flag-1)
    quick_sort(array,left_flag+1,end)

if __name__ == '__main__':
    array = []  # [69, 471, 106, 66, 149, 983, 160, 57, 792, 489, 764, 589, 909, 535, 972, 188, 866, 56, 243, 619]
    old_time = time.time()
    for i in range(50000):
        array.append(random.randrange(1000000))
    quick_sort(array,0,len(array)-1)
    print array
