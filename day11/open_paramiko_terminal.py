#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import paramiko
import os
import sys
import select
import socket

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

'''
# 利用sys.stdin,肆意妄为执行操作
# 用户在终端输入内容，并将内容发送至远程服务器
# 远程服务器执行命令，并将结果返回
# 用户终端显示内容
'''
while True:
    # 监视用户输入和服务器返回数据
    # sys.stdin 处理用户输入
    # chan 是之前创建的通道，用于接收服务器返回信息
    readable, writeable, error = select.select([chan, sys.stdin, ],[],[],1)  #坚挺chen和终端
    #只要发生变化，chan或者stdin或者都变化
    if chan in readable: #远端有变化后捕获到
        try:
            x = chan.recv(1024)
            #ssh连接后他发送接收数据也是通过socket来做的
            if len(x) == 0:
                print '\r\n************************ EOF ************************\r\n',
                break
            sys.stdout.write(x)#把内容输入到终端上
            sys.stdout.flush()
        except socket.timeout:
            pass
    if sys.stdin in readable: #当终端有输入捕获到之后
        inp = sys.stdin.readline() #把用户的那一行输入
        chan.sendall(inp)#发送命令至远端

chan.close()
tran.close()