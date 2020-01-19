#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'
import time
import random

maopao_list = [13, 22, 6, 99, 11]
'''
原理分析:
列表中有5个元素两辆进行比较，如果左边的值比右边的值大,就用中间值进行循环替换！
既然这样，我们还可以用一个循环把上面的循环进行在次循环，用表达式构造出内部循环！
'''

def handler(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            '''
            这里为什么要减1,我们看下如果里面有5个元素我们需要循环几次?最后一个值和谁对比呢?对吧!所以需要减1
            这里为什么减i这个i是循环的下标,如果我们循环了一次之后最后一只值已经是最大的了还有必要再进行一次对比吗?没有必要~
            '''
            print('left:%d' % array[j],'right:%d' % array[j+1])
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp



if __name__ == '__main__':
    handler(maopao_list)
    print(maopao_list)


'''
    array = []
    old_time = time.time()
    for i in range(50000):
        array.append(random.randrange(1000000))
    handler(array)
    print(array)
    print('Cost time is :',time.time() - old_time)
'''