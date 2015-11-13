#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json

add_infos = '{"backend": "cccc.oldboy.org","record":{"server": "100.1.7.10000000","weight": 20,"maxconn": 30}}'
add_info = json.loads(add_infos)
a = 'backend %s \n\t\tserver %s weight %s maxconn %s' % (add_info['backend'],\
add_info['record']['server'],add_info['record']['weight'],add_info['record']['maxconn'])
#上面的a是定义，如果没有用户输入的backend，就从字典模板中获取相关的值添加到配置文件中
b = '\t\tserver %s weight %s maxconn %s' % (add_info['record']['server'],\
add_info['record']['weight'],add_info['record']['maxconn'])
#上面的b的定义，如果backend存在直接从字典模板中获取相关的值添加到backend下面的配置文件中
backend_title = add_info['backend']
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
    #print backend_index
    #print backend_index[0]

    write_start = li[0:backend_index[0]-1]  #取出backend开头之前的数据并写入文件！
    for s in write_start:
        f2.write(s)
        f2.write('\n')
    for i in backend_index:  #循环backend的下标
        print i

'''
            w_start = backend_index[0]
            w_zanting = li.index(li[i])
            for m in li[w_start:w_zanting]:
                f2.write(m)
'''






'''
        if backend_title in li[i] and i != backend_index[-1]: #如果添加的backend在原配置文件中存在，那么在找到这个backend下标下面的server中添加server信息
            for u in li[i:backend_index[backend_index.index(i)+1]]:
                f2.write(u)
                f2.write('\n')
        if backend_title in li[i] and i == backend_index[-1]: #判断如果最后一行找到用户输入的backend就直接添加到备份文件
            for w in li[i:]:
                f2.write(w)
                f2.write('\n')
            f2.write(b)
        if backend_title not in li[i] and i == backend_index[-1]: #判断如果最后一行都没有找到用户输入的backend就直接添加到备份文件
            for w in li[i:]:
                f2.write(w)
                f2.write('\n')
                f2.write('\n')
            f2.write(a)
'''