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
from cmdb import views
urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    url(r'^lists/$', views.lists),
    url(r'^save_hostinfo/$', views.save_hostinfo),
    url(r'^del_hostinfo/$', views.del_hostinfo),
    url(r'^add/$', views.add),
    url(r'^logout/$', views.logout),
    url(r'', views.login),

]
