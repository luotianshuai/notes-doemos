#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info = raw_input('\033[33;1mplease input your backen\033[0m')\

#info = 'buy.oldboy.org'
info = 'www.oldboy.org'
#info = 'test.shuaige.org'
tim = []
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
    #print new_li
    for m,n in enumerate(new_li):
        if 'backend' in n :
            tim.append(m)
        if info in n :
            start_backend = m
            print start_backend
    print tim
    start_index =  tim.index(start_backend)
    print start_index
    if start_backend == tim[-1]:  #判断是否是最后一个backend
        print '\033[32;1m这是最后一行\033[0m'
        print new_li[m-1:]
    else:
        print '\033[32;1m这不是最后一行\033[0m'
        backend_info =  new_li[tim[start_index]:tim[start_index+1]]
    for l in backend_info:
        print l
    '''
    for s in range(len(tim)):
        print s
'''