#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

#一 enumerrate函数
#
# #一般情况下对一个列表话属组记要遍历所以又要遍历元素时,会这样写
check_list = [1,2,3,4,5,6,7]

for i in range (0,len(check_list)):
    print(i,len(check_list))

# #但是这种方法有些累赘,使用内置的enumerrate函数会有更直接更优美的做法
'''
emumerate会降属组或列表组成一个索引序列,使我们在获取索引和索引内容的时候更加方便
内部实现:
    def enumerate(collection):
        'Generates an indexed series:  (0,coll[0]), (1,coll[1]) ...'
        i = 0
        it = iter(collection)
        while 1:
            yield (i, it.next())
            i += 1
'''

for index,list_value in enumerate(check_list):
    print(index,list_value)

#二 有序字典

from collections import OrderedDict

disc_items = (
    (1,'中国'),
    (2,'美国'),
    (3,'发过'),
)
print(type(disc_items))

ordered_dic = OrderedDict(disc_items)
print(type(ordered_dic))

for k,v in ordered_dic.items():
    print(k,v)


'''
之前有个同学问我一个问题,有序字典!他想用下标去取值,这里是需要记录下,有序字典的有序并不是说他可以给字典设置下标通过下标去取值
而是在你往字典添加值得时候给你做一个对应关系:
1 {1,'中国',}
2 {1,'中国',2:'美国'}

ordered_dic = OrderedDict(disc_items)  这句不太懂得可以看下这个例子:

disc_items = (
    (1,'中国'),
    (2,'美国'),
    (3,'发过'),
)

disc_items = dict(disc_items)
print(disc_items)
'''