#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'

import tornado.ioloop
import tornado.web
from hashlib import sha1
import os, time
import re


class MainForm(object):
    def __init__(self):
        self.host = "(.*)"
        self.ip = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"
        self.port = '(\d+)'
        self.phone = '^1[3|4|5|8][0-9]\d{8}$'

    def check_valid(self, request):
        form_dict = self.__dict__
        for key, regular in form_dict.items():
            post_value = request.get_argument(key)
            # 让提交的数据 和 定义的正则表达式进行匹配
            ret = re.match(regular, post_value)
            print key,ret,post_value


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
    def post(self, *args, **kwargs):
        # obj = MainForm()
        # result = obj.check_valid(self)
        # self.write('ok')
        flag = True
        obj = MainForm()
        for k,v in obj.__dict__.items():
            if re.match(v,self.get_argument(k)):
                pass
            else:
                flag = False
        if flag:
            self.write('ok')
        else:
            self.write('error')


settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh',
    'login_url': '/login'
}

application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()