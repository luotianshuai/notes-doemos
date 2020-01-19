# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
# __author__ == 'LuoTianShuai'
import sys
import time
import pika

# 远程主机的RabbitMQ Server设置的用户名密码
credentials = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.31.123", 5672, "/", credentials))

# 创建通道
channel = connection.channel()

# 声明Exchanges
channel.exchange_declare(exchange="logs",
                         exchange_type="fanout")
"""
这里可以看到我们建立连接后,就声明了Exchange,因为把消息发送到一个不存在的Exchange是不允许的,
如果没有消费者绑定这个,Exchange消息将会被丢弃这是可以的因为没有消费者
"""
# 添加消息
message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange="logs",  # 将消息发送至Exchange为logs绑定的队列中
                      routing_key="",
                      body=message,)

print(" [x] Sent %r" % message)
# 关闭通道
connection.close()
