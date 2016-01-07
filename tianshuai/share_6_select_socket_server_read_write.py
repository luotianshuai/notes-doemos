#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import select
import socket
import Queue
import time

sk = socket.socket()
sk.bind(('127.0.0.1',6666))
sk.listen(5)
sk.setblocking(False) #定义非阻塞
inputs = [sk,]  #定义一个列表，select第一个参数监听句柄序列,当有变动是，捕获并把socket server加入到句柄序列中
outputs = [] #定义一个列表，select第二个参数监听句柄序列，当有值时就捕获，并加入到句柄序列
message = {}
#message的样板信息
#message = {
#    'c1':队列，[这里存放着用户C1发过来的消息]例如:[message1,message2]
#    'c2':队列，[这里存放着用户C2发过来的消息]例如:[message1,message2]
#}


while True:
    readable_list, writeable_list, error_list = select.select(inputs,outputs,[],1)
    #文件描述符可读 readable_list    只有第一个参数变化时候才捕获，并赋值给readable_list
    #文件描述符可写 writeable_list   只要有值，第二个参数就捕获并赋值给writeable_list
    #time.sleep(2)
    print 'inputs:',inputs
    print 'output:'
    print 'readable_list:',readable_list
    print 'writeable_list:',writeable_list
    print 'message',message
    for r in readable_list: #当readable_list有值得时候循环
        if r == sk:  #判断是否为链接请求变化的是否是socket server
            conn,addr = r.accept() #获取请求
            inputs.append(conn) #把客户端对象（句柄）加入到inputs里
            message[conn] = Queue.Queue() #并在字典里为这个客户端连接建立一个消息队列
        else:
            client_data = r.recv(1024) #如果请求的不是sk是客户端接收消息
            if client_data:#如果有数据
                outputs.append(r)#把用户加入到outpus里触发select第二个参数
                message[r].put(client_data)#在指定队列中插入数据
            else:
                inputs.remove(r)#没有数据，删除监听链接

    for w in writeable_list:#如果第二个参数有数据

        try:
            data = message[w].get_nowait()#去指定队列取数据 并且不阻塞
            w.sendall(data) #返回请求输入给client端
        except Queue.Empty:#反之触发异常
            del message[w]   #如果异常时移除
            pass
        outputs.remove(w) #因为第二个参数有值得时候就触发捕获值，所以使用完之后需要移除它

    print '%s' %('-' * 40)