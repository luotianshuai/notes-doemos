#/usr/bin/env python
#-*- coding:utf-8 -*-
import time
import socket
import select
#创建socket对象
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.setsockopt
#设置监听的IP与端口
sk.bind(('127.0.0.1',6666))
#设置client最大等待连接数
sk.listen(5)
sk.setblocking(False) #这里设置setblocking为Falseaccept将不在阻塞，但是如果没有收到请求就会报错
while True:
    readable_list, writeable_list, error_list = select.select([sk,],[],[],2)  #监听第一个列表的文件描述符，如果里面有文件描述符发生改变既能捕获并放到readable_list中
    for r in readable_list:    #如果是空列表将不执行，如果是空列表。将执行。
        conn,address = r.accept()
        print address