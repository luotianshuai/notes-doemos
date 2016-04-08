#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time

from wsgiref.simple_server import make_server
from jinja2 import Template

current_time = str(time.time())

def index():
    data = open('html/index.html').read()

    template = Template(data)
    result = template.render(
        name = 'luotianshuai',
        age = '18',
        time = current_time,
        user_list = ['tianshuai','tim','shuaige'],
        num = 1
    )

    #同样是替换为什么用jinja,因为他不仅仅是文本的他还支持if判断 & for循环 操作


    return result.encode('utf-8') #这里需要注意因为默认是的unicode的编码所以设置为utf-8

def shuaige():
    data = open('html/shuaige.html').read()
    return data


url_list = [
    ('/index/',index),
    ('/shuaige/',shuaige),
]


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #根据RUL不同,返回不同的字符
    #1/获取URL
    #根据URL的不同做不同的处理

    request_url = environ['PATH_INFO']
    print environ['PATH_INFO']
    for url in url_list:
        if request_url in url[0]:
            return url[1]()
    else:
        return "<h1>404</h1>"


if __name__ == '__main__':
    httpd = make_server('', 8003, RunServer)
    print "Serving HTTP on port 8003..."
    httpd.serve_forever()