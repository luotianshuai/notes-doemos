#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
#创建socket对象
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.setsockopt
#设置监听的IP与端口
sk.bind(('127.0.0.1',6666))
#设置client最大等待连接数
sk.listen(5)

while True: #循环
    print 'waiting client connection .......'
    #只有accept & recv 会阻塞，这里accept阻塞，直到有client连接过来
    #connection代表客户端对象，address是客户端的IP
    connection,address = sk.accept()
    #等待接收客户端信息
    client_messge = connection.recv(1024)
    #打印客户端信息
    print 'client send messge',client_messge
    #发送回执信息给client 收发必须相同
    connection.sendall('hello Client this server')
    connection.send()
    #关闭和client的连接
    connection.close()