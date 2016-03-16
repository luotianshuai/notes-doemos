# coding:utf-8
from django.shortcuts import render
from cmdb import forms
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'shuai' and password == '123':
            result = request.session.get('IS_LOGIN', None)
            print result
            request.session['IS_LOGIN'] = True
            return redirect('/index/')
    obj = forms.LoginForm()
    # 如果登录成功，写入session，跳转index
    return render(request, 'account/login.html', {'model': obj})


def index(request):
    '''
    如果用户已经登录
    '''
    is_login = request.session.get('IS_LOGIN',False)
    if is_login:
        return render(request, 'home/index.html')
    else:
        return redirect('/login/')






def lists(request):
    return render(request, 'asset/lists.html')

def add(request):
    return render(request, 'asset/import_single.html')


def user_list(request,v2,v1):
    print v2 , v1
    return HttpResponse(v1+v2)

