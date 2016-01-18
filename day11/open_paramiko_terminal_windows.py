#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import paramiko
import sys
import threading

tran = paramiko.Transport(('192.168.0.111', 22,))
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
sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")

def writeall(sock):
    while True:
        data = sock.recv(256)
        '''
        SSH发送数据的也是通过socket进行发送数据的，那么我们就可以使用socket来获取远程机器发送回来的数据。
        while循环一直接收数据，sock.recv(256)是阻塞的只有数据过来的时候才会继续走。
        '''
        if not data:
            sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
            sys.stdout.flush()
            break
        sys.stdout.write(data)
        sys.stdout.flush()

writer = threading.Thread(target=writeall, args=(chan,)) #创建了一个线程，去执行writeall方法，参数为chan（建立的SSH连接）
writer.start()

try:
    while True: #主线程循环
        d = sys.stdin.read(1)  #一直监听用户的输入，输入一个发送一个
        if not d:
            break
        chan.send(d)
except EOFError:
    # user hit ^Z or F6
    pass

chan.close()
tran.close()