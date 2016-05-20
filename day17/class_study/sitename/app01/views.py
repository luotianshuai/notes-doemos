#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse



def login(request):

    print request.method
    if request.method == "POST":
        input_emaill = request.POST['email']
        input_pwd = request.POST['pwd']
        if input_emaill == 'luotianshuai@qq.com' and input_pwd == '123':
            from django.shortcuts import redirect
            return redirect("/son/")
        else:
            return redirect(request,'login.html',{'status':'user or password error'},)

    return render(request,'login.html')




def son(request):
    return render(request,'son1.html')

dic = { 'name':'luotianshuai','age':'18'}


def home(request):
    # return HttpResponse('OK')
    return render(request,'home.html',dic)