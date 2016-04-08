#!//usr/bin/env python
#-*- coding:utf-8 -*-

from django.shortcuts import render,HttpResponse
from app01.forms import account as AccountForm
from app01 import models



def login(request):
    obj = AccountForm.LoginForm(request.POST)
    if request.method == 'POST':
        return render(request,'account/login.html',{'obj':obj})
    return render(request, 'account/login.html',{'obj':obj})

def useradd(request):
    #添加用户类型
    models.UserType.objects.create(typelist='超级用户')
    models.UserType.objects.create(typelist='金牌用户')
    models.UserType.objects.create(typelist='普通用户')
    #添加用户组
    models.UserGroup.objects.create(caption='CEO',user_type_id=1)
    models.UserGroup.objects.create(caption='CFO',user_type_id=2)
    models.UserGroup.objects.create(caption='CTO',user_type_id=3)
    #添加主机
    models.Host.objects.create(hostname='a01.shuaige.com',ip='1.1.1.1',user_group_id=1)
    models.Host.objects.create(hostname='a02.shuaige.com',ip='2.2.2.2',user_group_id=2)
    models.Host.objects.create(hostname='a03.shuaige.com',ip='3.3.3.3',user_group_id=3)
    return HttpResponse('OK')