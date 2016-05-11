#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bottle import template, Bottle,SimpleTemplate
root = Bottle()


def custom():
    return '123123'


@root.route('/hello/')
def index():
    # 默认情况下去目录：['./', './views/']中寻找模板文件 hello_template.html
    # 配置在 bottle.TEMPLATE_PATH 中
    return template('hello_template.html', name='tianshuai', shuaige=custom)

root.run(host='localhost', port=8080)