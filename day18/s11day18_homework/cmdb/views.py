# coding:utf-8
from django.shortcuts import render
from cmdb import forms
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from cmdb import models
from backend.decorators.login_auth import login_auth

# Create your views here.



def login(request):
    obj = forms.LoginForm()
    if request.method == 'POST':
        #获取用户输入
        login_form = forms.LoginForm(request.POST)
        #判断用户输入是否合法
        if login_form.is_valid():#如果用户输入是合法的
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_info_list = models.UserInfo.objects.all()
            for i in user_info_list:
                if username == i.email and password == i.passwords:
                    request.session['auth_user'] = username
                    return redirect('/index/')
            else:
                return render(request,'account/login.html',{'model': obj,'backend_autherror':'用户名或密码错误'})
        else:
            error_msg = login_form.errors.as_data()
            return render(request,'account/login.html',{'model': obj,'errors':error_msg})

    # 如果登录成功，写入session，跳转index
    return render(request, 'account/login.html', {'model': obj})


@login_auth
def index(request):
    username = request.session['auth_user']
    return render(request, 'home/index.html',{'username':username})


@login_auth
def lists(request):
    username = request.session['auth_user']
    host_info = models.HostInfo.objects.all()
    return render(request, 'asset/lists.html',{'username':username,'hostinfo_list':host_info,})



def add(request):
    return render(request, 'asset/import_single.html')



def logout(request):
    del request.session['auth_user']
    return redirect('/login/')