#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'

import paramiko

'''
第一种方法
'''

ssh = paramiko.SSHClient() #创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #允许连接不在know_hosts文件中的主机
ssh.connect(hostname='192.168.7.100',port=22,username='root',password='nihao123!')
stdin,stdout,stderror = ssh.exec_command('ifconfig，美女，') #执行命令

print stdout.read() #获取命令结果
print stderror.read() #如果执行错误返回错误结果
ssh.close() #关闭连接


'''
第二种方法
'''

transport = paramiko.Transport(('192.168.7.100',22)) #创建一个连接对象
transport.connect(username='root',password='nihao123!')#调用transport对象中的连接方法

ssh = paramiko.SSHClient() #创建SSH对象
ssh._transport = transport #把ssh对象中的_transport 字段进行赋值为transport

stdin,stdout,stderr = ssh.exec_command('ifconfig') #执行命令

print stdout.read()
print stderr.read()

transport.close()


'''
第二种方法和第一种方法的区别！
第一种方法
ssh = paramiko.SSHClient()  他的内部的connect其实内部封装了Transport
        t = self._transport = Transport(sock, gss_kex=gss_kex, gss_deleg_creds=gss_deleg_creds)

在文件操作的时候只能用第二种方法
'''


