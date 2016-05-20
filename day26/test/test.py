#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'


import json

test_dic = {'name':'luotianshuai','age':18}
print '未dumps前类型为:',type(test_dic)
#dumps 将数据通过特殊的形式转换为所有程序语言都识别的字符串
json_str = json.dumps(test_dic)
print 'dumps后的类型为:',type(json_str)

#loads 将字符串通过特殊的形式转为python是数据类型

new_dic = json.loads(json_str)
print '重新loads加载为数据类型:',type(new_dic)

print '*' * 50

#dump 将数据通过特殊的形式转换为所有语言都识别的字符串并写入文件
with open('test.txt','w') as openfile:
    json.dump(new_dic,openfile)
    print 'dump为文件完成!!!!!'
#load 从文件读取字符串并转换为python的数据类型

with open('test.txt','rb') as loadfile:
    load_dic = json.load(loadfile)
    print 'load 并赋值给load_dic后的数据类型:',type(load_dic)

