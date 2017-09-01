# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
# __author__ == 'LuoTianShuai'
"""
生产者/发送方
"""
import sys
import pika

# 远程主机的RabbitMQ Server设置的用户名密码
credentials = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.31.123', 5672, '/', credentials))

# 创建通道
channel = connection.channel()

# 声明队列task_queue,RabbitMQ的消息队列机制如果队列不存在那么数据将会被丢掉,下面我们声明一个队列如果不存在创建
channel.queue_declare(queue='task_queue')

# 在队列中添加消息
message = ' '.join(sys.argv[1:]) or "Hello World!"
# 发送消息
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2, ))  # make message persistent

# 发送消息结束,并关闭通道
print(" [x] Sent %r" % message)
channel.close()
