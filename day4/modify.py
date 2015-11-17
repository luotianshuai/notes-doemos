#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json

'''
定义查看函数：
1、打开文件 循环文件
2、定义一个标志位：backend_flag = False
3、if line.strip() == ('backend %s') %backend:
      backend_flag = True
      continue
   找到已backend开头，并且后面跟上用户输入：www.oldboy.org
   然后把backend_flag 标志位设置为True，并且跳出此次循环！
4、if backend_flag and line.strip() ：
   fetch_list.append(line)
   如果标志位backend_flag为真并且不为空是就把这一行追加到列表
5、if backend_flag and line.strip().startswith('backend'):
       break
   如果标志位backend_flag 为真并且开头为backend跳出循环

解释：
   在循环文件中，定义了标志位为False时候，if backend_flag and line.strip().startswith('backend'): 不执行的！
   if backend_flag and line.strip(): 也是不执行的！
   只有当匹配到用户输入的backend匹配时，if line.strip() == ('backend %s') %backend: 现在backend_flag = True
   if backend_flag and line.strip(): 标志位为真，并且不为空时将执行，并且追加到列表中。

   当遇到下一个backend的时候，现在标志位（backend_flag现在是True）
   if backend_flag and line.strip().startswith('backend'):  这个就匹配上，将会退出整个循环！
       break

'''
def get_backend(backend):
    fetch_list = []
    with open('haproxy.conf') as f:
        backend_flag = False
        for line in f:
            if line.strip() == "backend %s" % backend:
                backend_flag = True
                continue
            if backend_flag and line.strip().startswith('backend'):
                break
            if backend_flag and line.strip():
                fetch_list.append(line)
    return fetch_list


'''
定义添加函数：
首先判断backend是否存在：
1、backend存在，只需添加记录
   1.1、记录存在，存在不添加退出
   2.2、不存在不存在，不存在添加记录
2、backend不存在，直接在后面添加backend和server记录

'''
def add_backend(backend):
    backend_title = backend.get('backend')
    current_title = 'backend %s' % backend_title
    current_record = '%sserver %s %s weight %s maxconn %s' % (" "*8,backend['record']['server'],backend['record']['server'],backend['record']['weight'],backend['record']['maxconn'])

    check_backend = get_backend(backend)
    if check_backend:
        if current_record in check_backend:
            return '\033[32;1m您添加的backend和record信息已存在！\033[0m'
    else:
        '''backend如果不存直接添加backend和server记录'''
        with open('haproxy.conf','r') as old_ha,open('haproxy.conf.new','w') as new_ha:
            for line in old_ha:
                new_ha.write(line)
            new_ha.write('\n'*2)
            new_ha.write(current_title)
            new_ha.write('\n')
            new_ha.write(current_record)
        return "\033[31;1m您添加的backend是新的已为您新增backend和记录！\033[0m"



if __name__ == '__main__':
    while True:
        print '''\033[34;1m\
输入1获取ha记录
输入2增加ha记录
输入3删除ha记录
输入0将退出程序\033[0m'''
        num = raw_input('\033[33;1m请输入您需要的功能：\033[0m')
        if num == '1':
            print '''
            查询功能测试：
            存在：www.oldboy.org 不存在：none.oldboy.org'''
            read = raw_input('\033[33;1m请输入您要查看的backend名称：\033[0m')
            get_info = get_backend(read)
            if get_info:
                for i in get_info:
                    print i
            else:
                print "\033[31;1m无法找到您输入的backend请检查：%s是否正确\033[0m" % read
        if num == '2':
            print '\033[32;1m输入添加测试：不存在：\033[33;1m{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 3000}}\033[0m\033[0m'
            print '\033[32;1m输入添加测试：backend存在record存在：\033[33;1m{"backend": "buy.oldboy.org","record":{"server": "100.1.7.10","weight": 20,"maxconn": 3000}}\033[0m\033[0m'
            print '\033[32;1m输入添加测试：backend存在record不存在：\033[33;1m{"backend": "buy.oldboy.org","record":{"server": "100.1.7.101","weight": 20,"maxconn": 3000}}\033[0m\033[0m'
            read = raw_input('\033[33;1m请输入您要添加的信息：\033[0m')
            read_new = json.loads(read)
            print add_backend(read_new)







