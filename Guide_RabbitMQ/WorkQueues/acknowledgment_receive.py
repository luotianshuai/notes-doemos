# !/usr/bin/env python3.5
# -*- coding:utf-8 -*-
# __author__ == 'LuoTianShuai'
import time
import pika

# 定义认证信息
credentials = pika.PlainCredentials("admin", "admin")
# 定义连接配置
connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.31.123", 5672, "/", credentials))
# 创建通道
channel = connection.channel()
# 创建队列
channel.queue_declare("task_queue")


# 订阅回调函数,这个订阅回调函数是由pika库来调用
def callback(ch, method, properties, body):
    """
    :param ch: 通道对象
    :param method: 消息方法
    :param properties: 
    :param body: 消息内容
    :return: None
    """
    print(" [x] Received %r" % (body,))
    time.sleep(2)
    print(" [x] Done")
    # 发送消息确认,确认交易标识符
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 定义消费者通道参数
channel.basic_consume(callback, queue="task_queue")

# 开始接收消息
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()