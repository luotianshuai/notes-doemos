#/usr/bin/env python
#-*- coding:utf-8 -*-

"""s11day18_homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from cmdb.views import account
from cmdb.views import home
from cmdb.views import asset

urlpatterns = [

    #账户操作登录登出
    url(r'^login/$', account.login),
    url(r'^logout/$', account.logout),

    #home操作
    url(r'^index/$', home.index),

    #资产信息操作
    url(r'^lists/$', asset.lists),
    url(r'^get_select/$', asset.get_select),
    url(r'^save_hostinfo/$', asset.save_hostinfo),
    url(r'^del_hostinfo/$', asset.del_hostinfo),
    url(r'^add/$', asset.add),

    #default url
    url(r'', account.login),

]
