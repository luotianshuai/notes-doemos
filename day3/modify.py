#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time

def get_backend(check_info):
    backend_index = []
    with open('haproxy.conf','r') as f:  #打开文件
        li  = []   #创建一个新列表，后续加入
        for i in f.readlines(): #循环列表
            i = i.strip('\n') #取消回车符
            li.append(i) #把读取的文件加入列表中
        for k,v in enumerate(li):#循环列表并指定下标
            if 'backend' in v and 'backend' == v[0:7]:
                backend_index.append(k) #把backend的所在的下标加入到列表中
        for i in backend_index:  #循环backend的下标
            if check_info in li[i] and i != backend_index[-1]: #如果发现info在li列表中的i=循环的下标中并且不是最后一个
                for i in  li[i:backend_index[backend_index.index(i)+1]]:#打印li中i下标所在行和backend_index中的i后面元素所在行
                    print i
                return ''
                #return [for i in li[i:backend_index[backend_index.index(i)+1]]:print i ]
            elif check_info in li[i] and i == backend_index[-1]:  #如果是最后一个打印所有
                return li[i:]  #打印行
        else:
            return '\033[32;1m对比起无法找到您输入的\033[31;1m%s\033[0m\033[32;1m的backend信息\033[0m' % check_info

def add_backend(add_info):
    backend_index = []
    with open('haproxy.conf','r') as f:  #打开文件
        li  = []   #创建一个新列表，后续加入
        for i in f.readlines(): #循环列表
            i = i.strip('\n') #取消回车符
            li.append(i) #把读取的文件加入列表中
        for k,v in enumerate(li):#循环列表并指定下标
            if 'backend' in v and 'backend' == v[0:7]:
                backend_index.append(k) #把backend的所在的下标加入到列表中
        for i in backend_index:  #循环backend的下标
            if add_info in li[i] and i != backend_index[-1]: #如果发现info在li列表中的i=循环的下标中并且不是最后一个
                for i in  li[i:backend_index[backend_index.index(i)+1]]:#打印li中i下标所在行和backend_index中的i后面元素所在行
                    print i
                return ''
                #return [for i in li[i:backend_index[backend_index.index(i)+1]]:print i ]
            elif add_info in li[i] and i == backend_index[-1]:  #如果是最后一个打印所有
                for i in li[i]:
                    print i
                    return ''
        else:
            return '\033[32;1m对比起无法找到您输入的\033[31;1m%s\033[0m\033[32;1m的backend信息\033[0m' % add_info





if __name__ == '__main__':
    print '''\033[34;1m\
输入1获取ha记录
输入2增加ha记录
输入3删除ha记录\033[0m'''

    while True:
        num = raw_input('\033[32;1m请输入序列号：\033[0m')
        if num == '1':
            read = raw_input('\033[033;1m请输入您要查找的backend：\033[0m')
            print get_backend(read)
        if num == '2':
            read = raw_input('\033[033;1m请输入您要增加的backend：\033[0m')

#www.oldboy.org