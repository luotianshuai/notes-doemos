#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import HttpResponse
from app01 import models
# Create your views here.

def user_info(request):
    models.UserInfo.objects.filter(username='luotianshuai',age='18')





    return HttpResponse('OK')

def user_type(request):
    # dic = {'caption':'CEO'}
    # models.UserType.objects.create(**dic)
    return HttpResponse('Ok')
