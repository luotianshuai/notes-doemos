#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import paramiko
import os
import sys
import select
import socket
import termios
import tty


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
# 获取原tty属性
oldtty = termios.tcgetattr(sys.stdin)
#打开文件

try:
    # 为tty设置新属性
    # 默认当前tty设备属性：
    #   输入一行回车，执行
    #   CTRL+C 进程退出，遇到特殊字符，特殊处理。

    # 这是为原始模式，不认识所有特殊符号
    # 放置特殊字符应用在当前终端，如此设置，将所有的用户输入均发送到远程服务器
    tty.setraw(sys.stdin.fileno()) #把远端更换为LINUX原始模式
    chan.settimeout(0.0)
    user_log = open('terminalnew_log','ab')
    while True:
        # 监视 用户输入 和 远程服务器返回数据（socket）
        # 阻塞，直到句柄可读
        r, w, e = select.select([chan, sys.stdin], [], [], 1)
        if chan in r:
            try:
                x = chan.recv(1024)
                if len(x) == 0:
                    user_log.close()
                    print '\r\n*** EOF\r\n',
                    break
                sys.stdout.write(x)
                sys.stdout.flush()
            except socket.timeout:
                pass
        if sys.stdin in r:
            x = sys.stdin.read(1)
            if len(x) == 0:
                break
            user_log.write(x)
            chan.send(x)

finally:
    # 重新设置终端属性
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
chan.close()
tran.close()