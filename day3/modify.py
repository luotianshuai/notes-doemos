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
            return '\033[32;1msorry we cant find \033[31;1m%s\033[0m\033[32;1m backend info\033[0m' % check_info

def add_backend(add_infos):
    add_info = json.loads(add_infos)
    a = 'backend %s\n\t\tserver %s weight %s maxconn %s' % (add_info['backend'],add_info['record']['server'],add_info['record']['weight'],add_info['record']['maxconn'])
    #上面的a是定义，如果没有用户输入的backend，就从字典模板中获取相关的值添加到配置文件中
    b = '\t\tserver %s weight %s maxconn %s' % (add_info['record']['server'],add_info['record']['weight'],add_info['record']['maxconn'])
    #上面的b的定义，如果backend存在直接从字典模板中获取相关的值添加到backend下面的配置文件中
    backend_title = add_info['backend']
    backend_index = []
    li = []   #创建一个新列表，后续加入
    with open('haproxy.conf','r') as f1,open('haproxy.conf.add','w') as f2: #打开文件
        for i in f1.readlines(): #循环列表
            i = i.strip('\n') #取消回车符
            li.append(i) #把读取的文件加入列表中
        for k,v in enumerate(li):#循环列表并指定下标
            if 'backend' in v and 'backend' == v[0:7]:
                backend_index.append(k) #把backend的所在的下标加入到列表中
        write_start = li[0:backend_index[0]-1]  #取出backend开头之前的数据并写入文件！
        for s in write_start:
            f2.write(s)
            f2.write('\n')
        li_backend = li[backend_index[0]:]#定位backend信息，并整合为一个列表。
        for i in li_backend:
            if backend_title not in i: #判断如果backend信息不在此次循环中那么写入至文件
                f2.write(i)
                f2.write('\n')
                #print i
                if i  == li_backend[-1]: #判断如果是最后一行backend信息都没有用户输入的backend信息那么添加新的backend
                    f2.write('\n')
                    f2.write(a)
                    return '\033[31;1msoory you add backend we not have ，will create new backend\033[0m'
            if backend_title in i: #判断如果有backend那么追加文件
                f2.write(i)
                f2.write('\n')
                f2.write(b)
                f2.write('\n')
                for m in li_backend[li_backend.index(i)+1:]: #追加剩下的信息至文件中
                    f2.write(m)
                    f2.write('\n')
                return '\033[32;1myou add backend has bin，will add server info\033[0m'

def del_backend(del_infos):
    del_info = json.loads(del_infos)
    a = del_info['backend']
    b = get_backend(a) #调用自己写的查看参数判断输入信息是否存在！不存在退出出提示，存在继续！
    if 'sorry' in b:
        return b
    del_server = del_info['record']['server']
    backend_title = del_info['backend']
    li = []
    backend_index = []
    with open('haproxy.conf','r') as f1,open('haproxy.conf.del','w') as f2: #打开文件
        for i in f1.readlines(): #循环列表
            i = i.strip('\n') #取消回车符
            li.append(i) #把读取的文件加入列表中
        for k,v in enumerate(li):#循环列表并指定下标
            if 'backend' in v and 'backend' == v[0:7]:
                backend_index.append(k) #把backend的所在的下标加入到列表中
        for i in backend_index:  #循环backend的下标
            if backend_title in li[i] and i != backend_index[-1]: #如果添加的backend在原配置文件中存在，那么在找到这个backend下标下面的server中删除server信息！
                for r,t in enumerate(li[i:backend_index[backend_index.index(i)+1]],i+1): #循环列表并定义下标名称为当前back的下标+1
                    if del_server in t:
                        del li[r-1]
                        print '\033[31;1myou server info is del and not last line\033[0m'
                        break
            if backend_title in li[i] and i == backend_index[-1]: #如果添加的backend在原配置文件中存在，那么在找到这个backend下标下面的server中删除server信息！
                for r,t in enumerate(li[i:backend_index[backend_index.index(i)+1]],i+1):
                    if del_server in t:
                        del li[r-1]
                        print '\033[31;1m you server info is del and is last line\033[0m'
                        break
        for h in li:
            f2.write(h)
            f2.write('\n')
        print '\033[31;1mwork done please check !\033[0m'
if __name__ == '__main__':

    while True:
        print '''\033[34;1m\
输入1获取ha记录
输入2增加ha记录
输入3删除ha记录
输入0将退出程序\033[0m'''
        num = raw_input('\033[32;1m请输入序列号：\033[0m')
        if num == '1':
            read = raw_input('\033[033;1m请输入您要查找的backend：\033[0m')
            print get_backend(read)
        if num == '2':
            read = raw_input('\033[033;1m请输入您要增加的backend：\033[0m')
            print add_backend(read)
        if num == '3':
            read = raw_input('\033[033;1m请输入你要删除的backend：\033[0m')
            print del_backend(read)
        if num == '0':
            break


#www.oldboy.org