#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
import json

def get_info(info):

    with open('haproxy.conf','r') as f:  #打开文件
        li = []   #创建一个新列表，后续加入
        tim = []
        for i in f.readlines(): #循环列表
            i = i.strip('\n') #取消回车符
            li.append(i) #把读取的文件加入列表中
        for k,v in enumerate(li,1):#循环列表并指定下标
            if v[0:7] == 'backend': #判断bakend所在行的下标
                break
        new_li = li[k-1:]   #取出backend的范围，并整合成一个列表
        #print new_li
        for m,n in enumerate(new_li):  #循环backend的列表
            if 'backend' in n :
                tim.append(m)  #把所有append的小标加入到列表中用来做判断
            if info in n :
                start_backend = m  #取出开始的backend！
        #print tim
        start_index =  tim.index(start_backend)
        print start_index
        if start_backend == tim[-1]:  #判断是否是最后一个backend
            print '\033[32;1m这是最后一行\033[0m'
            last_info = new_li[m-1:]
            for p in last_info:
                print p
        else:
            print '\033[32;1m这不是最后一行\033[0m'
            backend_info =  new_li[tim[start_index]:tim[start_index+1]] #取出正确的范围
            for s in backend_info:
                print s

if __name__ == '__main__':
    print '''\033[34;1m\
输入1获取ha记录
输入2增加ha记录
输入3删除ha记录\033[0m'''
    num = raw_input('\033[32;1m请输入序列号：\033[0m')
    if num == '1':
        read = raw_input('\033[033;1m请输入backend：\033[0m')
        print get_info(read)
#www.oldboy.org