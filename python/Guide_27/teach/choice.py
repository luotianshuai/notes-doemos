#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'


xuanze_list = [13, 22, 6, 99, 11]

print(range(len(xuanze_list)))

def handler(array):
    for i in range(len(array)):
        '''
        循环整个列表
        '''
        for j in range(i,len(array)):
            '''
            这里的小循环里,循环也是整个列表但是他的起始值是i,当这一个小循环完了之后最前面的肯定是已经排序好的
            第二次的时候这个值是循环的第几次的值比如第二次是1,那么循环的起始值就是array[1]
            '''
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
        # print(array)


if __name__ == '__main__':
    handler(xuanze_list)
    print(xuanze_list)