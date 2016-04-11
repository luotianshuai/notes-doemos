#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bottle import template, Bottle
from bottle import static_file
root = Bottle()

@root.route('/hello/')
def index():
    return template('<b>Root {{name}}</b>!', name="Alex")

import app01
import app02

root.mount('app01', app01.app01)
root.mount('app02', app02.app02)

root.run(host='localhost', port=8080)