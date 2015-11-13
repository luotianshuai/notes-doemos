#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
input_info = '{"backend": "test.shuaige.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}'
add_info = json.loads(input_info)


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
        if backend_title in li[i] and i != backend_index[-1]: #如果发现info在li列表中的i=循环的下标中并且不是最后一个
            for q in  li[i:backend_index[backend_index.index(i)+1]]:#打印li中i下标所在行和backend_index中的i后面元素所在行
                f2.write(q)
                f2.write('\n')
        elif backend_title in li[i] and i == backend_index[-1]:  #如果是最后一个打印所有
            for w in li[i:]:
                f2.write(w)
                f2.write('\n')
        else:
