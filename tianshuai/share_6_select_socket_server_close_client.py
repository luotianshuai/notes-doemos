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
inputs = [sk,] #将sk这个对象加入到列表中，并且赋值给inputs
#原因：看上例conn是客户端对象，客户是一直连接着呢，连接的时候状态变了，连接上之后，连接上之后，还是服务端的socket 有关吗？
#是不是的把他改为动态的？

while True:
    readable_list, writeable_list, error_list = select.select(inputs,[],[],1)  #把第一个参数设为列表动态的添加
    time.sleep(2) #测试使用
    print "inputs list :",inputs     #打印inputs列表，查看执行变化
    print "file descriptor :",readable_list #打印readable_list ，查看执行变化

    for r in readable_list:
        if r == sk:  #这里判断，如果是客户端连接过来的话他不是sk，如果是服务端的socket连接过来的话是sk
            conn,address = r.accept()
            inputs.append(conn)
            print address
        else:
        #如果是客户端，接受和返回数据
            client_data = r.recv(1024)
            if client_data:
                r.sendall(client_data)
            else:
                inputs.remove(r)#如果没有收到客户端端数据，则移除客户端句柄 因为，不管是正常关闭还是异常关闭，client端的系统底层都会发送一个消息