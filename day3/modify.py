#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
import json
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

def add_backend(add_infos):
    add_info = json.loads(add_infos)
    a = 'backend %s\n\t\tserver %s weight %s maxconn %s' % (add_info['backend'],add_info['record']['server'],add_info['record']['weight'],add_info['record']['maxconn'])
    #上面的a是定义，如果没有用户输入的backend，就从字典模板中获取相关的值添加到配置文件中
    b = '\t\tserver %s weight %s maxconn %s' % (add_info['record']['server'],add_info['record']['weight'],add_info['record']['maxconn'])
    #上面的b的定义，如果backend存在直接从字典模板中获取相关的值添加到backend下面的配置文件中
    backend_title = add_info['backend']
    backend_index = []
    li = []   #创建一个新列表，后续加入
    with open('haproxy.conf','r') as f1,open('haproxy.conf.new','w') as f2: #打开文件
        for i in f1.readlines(): #循环列表
            i = i.strip('\n') #取消回车符
            li.append(i) #把读取的文件加入列表中
        print li
        for k,v in enumerate(li):#循环列表并指定下标
            if 'backend' in v and 'backend' == v[0:7]:
                backend_index.append(k) #把backend的所在的下标加入到列表中
        write_start = li[0:backend_index[0]-1]  #取出backend开头之前的数据并写入文件！
        for s in write_start:
            f2.write(s)
            f2.write('\n')
        for i in backend_index:  #循环backend的下标
            if backend_title not in li[i] and i == backend_index[-1]: #判断如果最后一行找到用户输入的backend就直接添加到备份文件
                for w in li[i:]:
                    f2.write(w)
                    f2.write('\n')
                f2.write('\n')
                f2.write(a)
                print '\033[31;1mbackend不存在，已添加！\033[0m'
            if backend_title not in li[i] and i != backend_index[-1]: #如果没有找到用户输入的backend并且不是最后一个backend那么就添加backend的下标到下一个backend的下标的信息到备份文件！
                for q in  li[i:backend_index[backend_index.index(i)+1]]:
                    f2.write(q)
                    f2.write('\n')
            if backend_title in li[i]   #如果添加的backend在原配置文件中存在，那么在找到这个backend下标下面的server中添加server信息
                for u in li[i:backend_index[backend_index.index(i)+1]]:
                    f2.write(u)
                    f2.write('\n')
                f2.write(b)
                print '\033[32;1mbackend已存在存在，并且不在第一行，仅添加backend内的信息\033[0m'



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
            print add_backend(read)

#www.oldboy.org