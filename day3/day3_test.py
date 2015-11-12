#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info = raw_input('\033[33;1mplease input your backen\033[0m')\

#info = 'buy.oldboy.org'
info = 'www.oldboy.org'

with open('haproxy.conf','r') as f:  #打开文件
    li = []   #创建一个新列表，后续加入
    for i in f.readlines(): #循环列表
        i = i.strip('\n') #取消回车符
        li.append(i) #把读取的文件加入列表中
    #print li
    for k,v in enumerate(li,1):#循环列表并指定下标
        #print k,v
        if v[0:7] == 'backend': #判断bakend所在行的下标
            #print k
            break
    new_li = li[k-1:]
    for m in new_li:
        #print m
        if info in m :



'''
    new_li.append(li[k-1:])
    print new_li
    for m in new_li:
        print m
'''




'''
            if info in v :
                print k,v
'''



'''
        if info in v and v[0:6] == 'backen':
            print li[k-1:-3]
'''

'''
            print shuai.sort()
            for o in shuai:
                print o
'''
'''
            for m,n in enumerate(li[k+1:-1],1):
                print m,n

    print new_li
'''