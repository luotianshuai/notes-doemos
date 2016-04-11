#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bottle import template, Bottle

app02 = Bottle()


@app02.route('/hello/', method='GET')
def index():
    return 'app02'