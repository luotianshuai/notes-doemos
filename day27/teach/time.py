#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'
#
# #O(1)
#
# n = 100 #执行一次
# sum = (1+n) * n/2 #执行一次
# sum_1 = (n/2) - 10 #执行一次
# sum_2 = n*4 - 10 + 8 /2 #执行一次
#
#
# #O(n2)
#
# n = 100 #执行一次
#
# for i in range(n): #执行了n次
#     for q in range(n): #执行了n2
#         print(q) #执行了n2
#
#O(n)
# n =100 #执行一次
# a = 0 #执行一次
# b = 1#执行一次
# for i in range(n): #执行n次
#     s = a +b #执行n-1次
#     b =a #执行n-1次
#     a =s #执行n-1次
#O(log2n)
# n =100
# i = 1 #执行一次
# while i < n:
#     i +=1 #执行n次
#
#
#
#O(n3)
# n = 100
# for i in range(n):#执行了n次
#     for q in range(n):#执行了n^2
#         for e in range(n):#执行了n^3
#             print(e)#执行了n^3







