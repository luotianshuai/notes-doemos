#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import os
import time

'''
添加装饰器：
    去备份修改后的文件！
    判断是否生成了haproxy.conf.new,如果生成了，就进行备份！并提示用户！
'''

def file_back(func):
    def wrapper(*args,**kargs):
        outp_info = func(*args,**kargs)
        file_rename = 'haproxy.conf' + time.strftime("%Y%d%M%S")
        file = 'haproxy.conf.new'
        if os.path.exists(file):
            os.rename('haproxy.conf',file_rename)
            os.rename('haproxy.conf.new','haproxy.conf')
            print "\033[32;1m备份成功！您好原始文件已备份为：\033[0m\033[34;1m%s\033[0m" % file_rename
        return outp_info
    return wrapper

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
                fetch_list.append(line.strip())
    return fetch_list


'''
定义添加函数：
首先判断backend是否存在：
1、backend存在，只需添加记录
   1.1、记录存在，存在不添加提示退出
   2.2、记录不存在，在backend下添加记录
2、backend不存在，直接在后面添加backend和server记录

思路：
    如果backend存在

把文件分割为3部分：上、中、下   中 = 找到的backend和record信息
打开两个文件：第一个是原文件、第二个是新文件。
循环读第一个文件中的数据写到第二个文件中，当匹配到backend那里之后把backend写入到第二个文件中，并且循环写入找到backend中的
record信息写入到第二个文件中，然后在第二个文件中匹配的record的信息下面追加一个添加的record信息。为了防止他写入多次设置一个
标志位has_write = False当：上面的操作完成之后给他设置为True！之后if not has_write:这个就不匹配了。就只写了一遍，然后把下半部分
写入即可！


'''
@file_back
def add_backend(backend):
    backend_title = backend.get('backend')
    current_title = 'backend %s' % backend_title
    current_record = 'services %s %s weight %s maxconn %s' % (backend['record']['services'],backend['record']['services'],backend['record']['weight'],backend['record']['maxconn'])

    check_backend = get_backend(backend_title)
    if check_backend:
        '''如果backend存在'''
        if current_record in check_backend:
            '''backend存在并且记录存在直接提示推出'''
            return '\033[31;1m您添加的backend和record信息已存在！\033[0m'
        else:
            with open('haproxy.conf','r') as old_ha,open('haproxy.conf.new','w') as new_ha:
                add_flag = False
                has_write = False
                for line in old_ha:
                    if line.strip() == current_title:
                        new_ha.write(line)
                        add_flag = True
                        continue
                    if add_flag and line.strip().startswith('backend'):
                        add_flag = False
                    if add_flag:
                        if not has_write:
                            for line_new in check_backend:
                                new_ha.write("%s%s\n" % (" "*8,line_new))
                            new_ha.write("%s%s\n\n" % (" "*8,current_record))
                            has_write = True
                    else:
                        new_ha.write(line)
                return "\033[33;1mbackend存在并且record信息不存在，已添加record信息！\033[0m"

    else:
        '''backend如果不存直接添加backend和server记录'''
        with open('haproxy.conf','r') as old_ha,open('haproxy.conf.new','w') as new_ha:
            for line in old_ha:
                new_ha.write(line)
            new_ha.write('\n')
            new_ha.write(current_title)
            new_ha.write('\n')
            new_ha.write("%s%s"% (" "*8,current_record))
        return "\033[31;1m您添加的backend是新的已为您新增backend和记录！\033[0m"

'''
定义删除函数：
删除函数和添加函数基本上相同：
首先查找backend是否存在
1、backend不存在，直接退出并提示用户信息

2、backend存在
2.1、backned存在，record不存在提示用户信息record不存在
2.2、backend存在，record存在删除record，然后判断backend下是否还存在信息,如果不存在删除backend
'''
@file_back
def del_backend(backend):
    backend_title = backend.get('backend')
    current_title = 'backend %s' % backend_title
    current_record = 'services %s %s weight %s maxconn %s' % (backend['record']['services'],backend['record']['services'],backend['record']['weight'],backend['record']['maxconn'])
    check_backend = get_backend(backend_title)
    if check_backend:
        '''如果backend存在'''
        with open('haproxy.conf','r') as old_ha_del,open('haproxy.conf.new','w') as new_ha_del:
            del_flag = False
            has_write = False
            for line in old_ha_del:
                if line.strip() == current_title:
                    del_flag = True
                    continue
                if del_flag and line.strip().startswith('backend'):
                    del_flag = False
                if del_flag:
                    if not has_write:
                        if current_record in check_backend:
                            check_backend.remove(current_record)
                        else:
                            new_ha_del.write(current_title)
                            for line_new in check_backend:
                                new_ha_del.write("%s%s\n" % (" "*8,line_new))
                            has_write = True
                            #print "\033[31;1m您好backend下无法找到record信息！"
                            continue

                        if check_backend:
                            new_ha_del.write(current_title+'\n')
                            for line_new in check_backend:
                                new_ha_del.write("%s%s\n" % (" "*8,line_new))
                            new_ha_del.write('\n')
                            has_write = True
                            #print "\033[33;1m您好backend下的record已经删除，并且backend还有记录！\033[0m"
                        else:
                            #print "\033[31;1m您好backend下的record已经删除并且backend下没有记录，将要删除backend！\033[0m"
                            has_write = True
                            continue
                else:
                    new_ha_del.write(line)
            return "\033[32;1m删除完成\033[0m"
    else:
        return "\033[31;1m您输入的backend不存在\033[0m"


if __name__ == '__main__':
    while True:
        print '''\033[34;1m\
输入1获取ha记录
输入2增加ha记录
输入3删除ha记录
输入0将退出程序\033[0m'''
        num = raw_input('\033[33;1m请输入您需要的功能：\033[0m')
        if num == '1':
            print '''查询功能测试：
存在：www.oldboy.org buy.oldboy.org nb.oldboy.org  不存在：none.oldboy.org'''
            read = raw_input('\033[33;1m请输入您要查看的backend名称：\033[0m')
            get_info = get_backend(read)
            if get_info:
                for i in get_info:
                    print i
            else:
                print "\033[31;1m无法找到您输入的backend请检查：%s是否正确\033[0m" % read
        if num == '2':
            print '\033[32;1m输入添加测试：backend不存在：\033[33;1m{"backend": "test.oldboy.org","record":{"services": "100.1.7.9","weight": 20,"maxconn": 3000}}\033[0m\033[0m'
            print '\033[32;1m输入添加测试：backend存在record存在：\033[33;1m{"backend": "buy.oldboy.org","record":{"services": "100.1.7.10","weight": 20,"maxconn": 3000}}\033[0m\033[0m'
            print '\033[32;1m输入添加测试：backend存在record不存在：\033[33;1m{"backend": "buy.oldboy.org","record":{"services": "100.1.7.101","weight": 20,"maxconn": 3000}}\033[0m\033[0m'
            read = raw_input('\033[33;1m请输入您要添加的信息：\033[0m')
            read_new = json.loads(read)
            print add_backend(read_new)
        if num == '3':
            print '\033[32;1m输入删除测试：backend不存在：\033[33;1m{"backend": "test.oldboy.org","record":{"services": "100.1.7.9","weight": 20,"maxconn": 3000}}\033[0m\033[0m'
            print '\033[32;1m输入删除测试：backend存在record存在,且仅有一条record记录：\033[33;1m{"backend": "www.oldboy.org","record":{"services": "100.1.7.9","weight": 20,"maxconn": 3000}}\033[0m\033[0m'
            print '\033[32;1m输入删除测试：backend存在record存在,且有其他record记录：：\033[33;1m{"backend": "buy.oldboy.org","record":{"services": "100.1.7.10","weight": 20,"maxconn": 3000}}\033[0m\033[0m'
            print '\033[32;1m输入删除测试：backend存在record不存在：\033[33;1m{"backend": "buy.oldboy.org","record":{"services": "100.1.7.99","weight": 20,"maxconn": 3000}}\033[0m\033[0m'
            read = raw_input('\033[33;1m请输入您要删除的信息：\033[0m')
            read_new = json.loads(read)
            print del_backend(read_new)
        if num == '0':
            print "\033[32;1m欢迎下次使用\033[0m"
            break
