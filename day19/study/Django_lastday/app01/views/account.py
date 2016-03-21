#!//usr/bin/env python
#-*- coding:utf-8 -*-

from django.shortcuts import render
from app01.forms import account as AccountForm



def login(request):
    obj = AccountForm.LoginForm(request.POST)
    if request.method == 'POST':
        return render(request,'account/login.html',{'obj':obj})
    return render(request, 'account/login.html',{'obj':obj})
