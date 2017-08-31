# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
# __author__ == 'LuoTianShuai'
"""
生产者/发送消息方
"""
import pika

# 远程主机的RabbitMQ Server设置的用户名密码
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.31.123', 5672, '/', credentials))
"""
A virtual host holds a bundle of exchanges, queues and bindings. Why would you want multiple virtual hosts? 
Easy. A username in RabbitMQ grants you access to a virtual host…in its entirety.
So the only way to keep group A from accessing group B’s exchanges/queues/bindings/etc. 
is to create a virtual host for A and one for B. Every RabbitMQ server has a default virtual host named “/”. 
If that’s all you need, you’re ready to roll.

virtualHost is used as a namespace
for AMQP resources (default is \"/\"),so different applications could use multiple virtual hosts on the same AMQP server

[root@localhost ~]# rabbitmqctl list_permissions
Listing permissions in vhost "/" ...
admin	.	.	.
guest	.*	.*	.*
...done.

注：相当于在rabbitmq层面又加了一层域名空间的限制,每个域名空间是独立的有自己的Echange/queues等

"""
# 创建频道
channel = connection.channel()
# 声明队列hello,RabbitMQ的消息队列机制如果队列不存在那么数据将会被丢掉,下面我们声明一个队列如果不存在创建
channel.queue_declare(queue='hello')

channel.publish(exchange="", routing_key="hello", body="Hello World")




