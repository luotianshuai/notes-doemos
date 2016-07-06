#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        test = {'name':'luotianshuai'}
        self.render('index.html',name=test)

settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/',
}

application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()