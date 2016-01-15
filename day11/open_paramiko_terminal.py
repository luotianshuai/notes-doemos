#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import paramiko
import os

tran = paramiko.Transport(('192.168.7.100', 22,))
tran.start_client()

'''
#使用密钥认证
default_path = os.path.join(os.environ['root'], '.ssh', 'id_rsa')
key = paramiko.RSAKey.from_private_key_file(default_path)
tran.auth_publickey('root', key)
'''
tran.auth_password('root', 'nihao123!') #通过密码认证
chan = tran.open_session()# 打开一个通道
chan.get_pty()# 获取一个终端
chan.invoke_shell()# 激活器

#########
# 利用sys.stdin,肆意妄为执行操作
# 用户在终端输入内容，并将内容发送至远程服务器
# 远程服务器执行命令，并将结果返回
# 用户终端显示内容
#########

chan.close()
tran.close()