#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
from wsgiref.simple_server import make_server
from jinja2 import Template


def index():
    data = open('html/index.html').read()

    template = Template(data)
    result = template.render(
        name = 'luotianshuai',
        age = '18',
        time = str(time.time()),
        user_list = ['tianshuai','tim','shuaige'],
        num = 1
    )

    #同样是替换为什么用jinja,因为他不仅仅是文本的他还支持if判断 & for循环 操作

    #这里需要注意因为默认是的unicode的编码所以设置为utf-8
    return result.encode('utf-8')

def login():
    #读取html并返回
    data = open('html/login.html').read()
    return data


#1 定义一个列表,上面定义函数
url_list = [
    #这里吧URL和函数做一个对应
    ('/index/',index),
    ('/login/',login),
]


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #根据url的不同,返回不同的字符串
    #1 获取URL[URL从哪里获取?当请求过来之后执行RunServer,wsgi给咱们封装了这些请求,这些请求都封装到了,environ & start_response]
    request_url = environ['PATH_INFO']
    #2 根据URL做不同的相应
    #print environ #这里可以通过断点来查看它都封装了什么数据

    #循环这个列表
    for url in url_list:
        #如果用户请求的url和咱们定义的rul匹配
        if request_url == url[0]:
            print url
            return url[1]()
            #执行里面的方法
    else:
        #url_list列表里都没有返回404
        return '404'

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()