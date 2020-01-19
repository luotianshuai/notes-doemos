#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'


import random
import time
chaoru_list = [69, 471, 106, 66, 149, 983, 160, 57, 792, 489, 764, 589, 909, 535, 972, 188, 866, 56, 243, 619]

def handler(array):
    for i in range(1,len(array)):
        position = i #刚开始往左边走的第一个位置
        current_val = array[i] #先把当前值存下来
        while position > 0 and current_val < array[position -1]:
            '''
            这里为什么用while循环,咱们在判断左边的值得时候知道他有多少个值吗?不知道,所以用while循环
            什么时候停下来呢?当左边没有值得时候,或者当他大于左边的值得时候!
            '''
            array[position] = array[position - 1] #如果whille条件成立把当前的值替换为他上一个值
            '''
            比如一个列表:
            [3,2,4,1]
            现在循环到 1了,他前面的元素已经循环完了
            [2,3,4] 1

            首先我们记录下当前这个position的值 = 1
            [2,3,4,4] 这样,就出一个位置了
            在对比前面的3,1比3小
            [2,3,3,4] 在替换一下他们的值
             在对比2
            [2,2,3,4]
            最后while不执行了在进行替换'array[position] = current_val  #把值替换'
            '''
            position -= 1
        #当上面的条件都不成立的时候{左边没有值/左边的值不比自己的值小}
        array[position] = current_val  #把值替换


if __name__ == '__main__':
    handler(chaoru_list)
    print(chaoru_list)

'''
    array = []#[69, 471, 106, 66, 149, 983, 160, 57, 792, 489, 764, 589, 909, 535, 972, 188, 866, 56, 243, 619]
    old_time = time.time()
    for i in range(50000):
        array.append(random.randrange(1000000))
    handler(array)
    print(array)
    print('Cost time is :',time.time() - old_time)
'''