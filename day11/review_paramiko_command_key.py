#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'

import paramiko
private_key = paramiko.RSAKey.from_private_key_file('id_rsa.pub')

ssh = paramiko.SSHClient()#创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #允许连接不在know_host文件中的的主机
ssh.connect(hostname='192.168.7.100',port=22,username='root',pkey=private_key) #连接服务器
stdin,stdout,stderr = ssh.exec_command('ifconfig') #执行命令
print stdout.read() #获取命令执行结果
ssh.close()