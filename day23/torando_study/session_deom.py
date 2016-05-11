#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
from hashlib import sha1
import os, time

session_container = {}

create_session_id = lambda: sha1('%s%s' % (os.urandom(16), time.time())).hexdigest()


class Session(object):

    session_id = "__sessionId__"

    def __init__(self, request):
        #当你请求过来的时候,我先去get_cookie看看有没有cookie!目的是看看有没有Cookie如果有的话就不生成了,没有就生成!
        session_value = request.get_cookie(Session.session_id)
        #如果没有Cookie生成Cookie[创建随机字符串]
        if not session_value:
            self._id = create_session_id()
        else:
            #如果有直接将客户端的随机字符串设置给_id这个字段,随机字符串封装到self._id里了
            self._id = session_value
        #在给它设置一下
        request.set_cookie(Session.session_id, self._id)

    def __getitem__(self, key):
        ret = None
        try:
            ret =  session_container[self._id][key]
        except Exception,e:
            pass
        return ret


    def __setitem__(self, key, value):
        #判断是否有这个随机字符串
        if session_container.has_key(self._id):
            session_container[self._id][key] = value
        else:
            #如果没有就生成一个字典
            '''
            类似:随机字符串:{'IS_LOGIN':'True'}
            '''
            session_container[self._id] = {key: value}

    def __delitem__(self, key):
        del session_container[self._id][key]


class BaseHandler(tornado.web.RequestHandler):

    def initialize(self):
        '''
        这里initialize的self是谁?
        obj = LoginHandler()
        obj.initialize() ==>这里LoginHandler这个类里没有initialize这个方法,在他父类里有
        所以initialize得self就是LoginHandler的对象
        '''
        self.my_session = Session(self) #执行Session的构造方法并且把LoginHandler的对象传过去
        '''
        这个self.my_session = Session()
        看这个例子:
        self.xxx = '123'  在这里创建一个对象,在LoginHandler中是否可以通过self.xxx去访问123这个值?
        可以,因为self.xxx 是在get之前执行的,他们俩的对象都是LoginHandler对象
        '''

class MainHandler(BaseHandler):

    def get(self):
        ret = self.my_session['is_login']
        if ret:
            self.write('index')
        else:
            self.redirect("/login")

class LoginHandler(BaseHandler):
    def get(self):
        '''
        当用户访登录的时候我们就得给他写cookie了,但是这里没有写在哪里写了呢?
        在哪里呢?之前写的Handler都是继承的RequestHandler,这次继承的是BaseHandler是自己写的Handler
        继承自己的类,在类了加扩展initialize! 在这里我们可以在这里做获取用户cookie或者写cookie都可以在这里做
        '''
        '''
        我们知道LoginHandler对象就是self,我们可不可以self.set_cookie()可不可以self.get_cookie()
        '''
        # self.set_cookie()
        # self.get_cookie()

        self.render('login.html', **{'status': ''})

    def post(self, *args, **kwargs):
        #获取用户提交的用户名和密码
        username = self.get_argument('username')
        password = self.get_argument('pwd')
        if username == 'wupeiqi' and password == '123':
            #如果认证通过之后就可以访问这个self.my_session对象了!然后我就就可以吧Cookie写入到字典中了,NICE
            self.my_session['is_login'] = 'true'

            '''
            这里用到知识点是类里的:
            class Foo(object):
                def __getitem__(self,key):
                    print '__getitem__',key

                def __setitem__(self,key,value):
                    print '__setitem__',key,value

                def __delitem__(self,key):
                    print '__delitem__',key

            obj = Foo()
            result = obj['k1'] #自动触发执行  __getitem__
            obj['k2'] = 'wupeiqi' #自动触发执行 __setitem__
            del obj['k1'] #自动触发执行  __delitme__

            '''

            self.redirect('/index')
        else:
            self.render('login.html', **{'status': '用户名或密码错误'})



settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh',
    'login_url': '/login'
}

application = tornado.web.Application([
    #创建两个URL 分别对应  MainHandler  LoginHandler
    (r"/index", MainHandler),
    (r"/login", LoginHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()