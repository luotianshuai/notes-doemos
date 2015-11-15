#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import os

def fetch(backend):
    with open('haproxy.conf') as obj:
        backend_list = []
        flag = False
        for line in obj:
            #line 每一行
            if line.strip() == 'backend %s' % backend:
                flag = True
                continue
            if flag and line.strip() == line.strip().startswith('backend'):
                break
            if flag and line.strip():
                backend_list.append(line)
        return backend_list

'''
    dict_info = {
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }
'''

def add1(dict_info):
    backend_title = dict_info.get('backend')
    current_title = "backend %s" % backend_title
    current_record = "server %s %s weight %s maxconn %s " %(dict_info['record']['server'],dict_info['record']['server'],\
    dict_info['record']['weight'],dict_info['record']['maxconn'])
    #获取定制backend下的所有记录
    fetch_list = fetch(backend_title)
    if fetch_list:
        pass #存在backend，则只需在添加
    else:
        pass #不存在backend，添加记录和backend
        #current title,creent_record
        with open('ha') as read_obj,open('ha.new','w') as write_obj:
            for line in read_obj:
                write_obj.write(line)
            write_obj.write(current_title)
            write_obj.write(current_record)
    os.rename('ha','ha.bak')
    os.rename('ha.new','ha')



if __name__ == '__main__':
    print fetch('aaa.oldboy.org')
    s = '''{
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }'''
    #如过想用上面的这种字符串的格式输出给python的话需要加三引号！！！！注意
    data_dict = json.loads(s)
    add1(data_dict)