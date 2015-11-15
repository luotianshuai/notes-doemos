#!/usr/bin/env pytohon
#-*- coding:utf-8 -*-
'''
li = [13,22,6,99,11]

for m in range(4):
    num1 = li[m]
    num2 = li[m+1]
    if num1 > num2:
        temp = li[m]
        li[m] = num2
        li[m+1] = temp
print  li
for m in range(3):
    num1 = li[m]
    num2 = li[m+1]
    if num1 > num2:
        temp = li[m]
        li[m] = num2
        li[m+1] = temp
print  li
for m in range(2):
    num1 = li[m]
    num2 = li[m+1]
    if num1 > num2:
        temp = li[m]
        li[m] = num2
        li[m+1] = temp
print  li
for m in range(1):
    num1 = li[m]
    num2 = li[m+1]
    if num1 > num2:
        temp = li[m]
        li[m] = num2
        li[m+1] = temp
print  li
'''
'''冒泡算法for循环'''
'''
#第一种方法
#第二种方法，在第二天的博客里有！
li = [13,22,6,99,11]
for n in range(1,len(li)):
    for m in range(len(li)-n):
        num1 = li[m]
        num2 = li[m+1]
    if num1 > num2:
        temp = li[m]
        li[m] = num2
        li[m+1] = temp
print li

冒泡算法：
列表中有5个元素两辆进行比较，然后用中间值进行循环替换！
既然这样，既然这样我们还可以用一个循环把上面的循环进行在次循环，用表达式构造出内部循环！

'''

li = [13,22,6,99,11]
