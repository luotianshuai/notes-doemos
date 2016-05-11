#!/usr/bin/env python
#-*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
#封装了配置文件和路由映射
application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    #创建一个Socket Server 然后监听8888端口
    application.listen(8888)
    #监听Socket Server ==> select,epoll监听
    tornado.ioloop.IOLoop.instance().start()
