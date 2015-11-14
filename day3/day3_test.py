#!/usr/bin/env python
#-*- coding:utf-8 -*-
del_infos = '{"backend": "bbb.oldboy.org","record":{"server": "100.1.7.90","weight": 20,"maxconn": 3000}}'
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
            if backend_title in li[i] and i != backend_index[-1]: #如果添加的backend在原配置文件中存在，那么在找到这个backend下标下面的server中添加server信息
                for u in li[i:backend_index[backend_index.index(i)+1]]:
                    if del_server in u:
                        print li[i:backend_index[backend_index.index(i)+1]].index(li[i:backend_index[backend_index.index(i)+1]])

            if backend_title in li[i] and i == backend_index[-1]: #判断如果最后一行找到用户输入的backend就直接添加到备份文件
                for w in li[i:]:
                    f2.write(w)
                    f2.write('\n')
                f2.write(b)
                print '\033[32;1m您添加的backend已存在并且在最后一行，添加server信息完成\033[0m'


if __name__ == '__main__':
    print del_backend()