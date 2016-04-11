#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bottle import template, Bottle

app01 = Bottle()

@app01.route('/hello/', method='GET')
def index():
    return template('<b>App01</b>!')