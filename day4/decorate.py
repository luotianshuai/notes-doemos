#!/usr/bin/env python
#-*-  coding:utf-8 -*-

def wrapper(func):  #装饰器定义
    if login('alex'):
        return func

def login(user):   #新加功能
    if user == 'alex':
        return True
    else:
        print "Invalid username"

def redirect(url):pass

@wrapper
def home():
    print 'showing the home page'
def host_list():
    print 'showing the host list page'
def user_list():
    print 'show the user list page'

home()