#!/usr/bin/env python
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
from cmdb import urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #因为就这一个APP所以直接把所有的请求转发值cmdb app中的urls里,并在cmdb.urls里在设置默认的跳转
    url(r'', include("cmdb.urls")),

]
