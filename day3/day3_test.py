#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import re

add_infos = '{"backend": "eee.oldboy.org","record":{"server": "100.1.7.10000000","weight": 20,"maxconn": 30}}'
add_info = json.loads(add_infos)
a = 'backend %s \n\t\tserver %s weight %s maxconn %s' % (add_info['backend'],\
add_info['record']['server'],add_info['record']['weight'],add_info['record']['maxconn'])
#上面的a是定义，如果没有用户输入的backend，就从字典模板中获取相关的值添加到配置文件中
b = '\t\tserver %s weight %s maxconn %s' % (add_info['record']['server'],\
add_info['record']['weight'],add_info['record']['maxconn'])
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
    #print backend_index
    #print backend_index[0]

    write_start = li[0:backend_index[0]-1]  #取出backend开头之前的数据并写入文件！
    for s in write_start:
        f2.write(s)
        f2.write('\n')
    li_backend= li[backend_index[0]:]
    for i in li_backend:
        if backend_title not in i:
            f2.write(i)
            f2.write('\n')
            print 'hello'
    '''
    for i in li[backend_index[0]:]:
        if backend_title not in i:
            f2.write(i)
            f2.write('\n')
'''