from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from app01 import views


urlpatterns = [
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^home/', views.home),
    url(r'^user_list/', views.user_list),
    url(r'^ajax_data/', views.ajax_data),
]
