# coding:utf-8
from django.shortcuts import render
from cmdb.forms import account as AccountForm
from django.shortcuts import redirect
from cmdb import models

# Create your views here.



def login(request):
    #获取用户输入
    login_form = AccountForm.LoginForm(request.POST)
    if request.method == 'POST':
        #判断用户输入是否合法
        if login_form.is_valid():#如果用户输入是合法的
            username = request.POST.get('username')
            password = request.POST.get('password')
            if models.UserInfo.objects.get(username=username) and models.UserInfo.objects.get(username=username).password == password:
                    request.session['auth_user'] = username
                    return redirect('/index/')
            else:
                return render(request,'account/login.html',{'model': login_form,'backend_autherror':'用户名或密码错误'})
        else:
            error_msg = login_form.errors.as_data()
            return render(request,'account/login.html',{'model': login_form,'errors':error_msg})

    # 如果登录成功，写入session，跳转index
    return render(request, 'account/login.html', {'model': login_form})


def logout(request):
    del request.session['auth_user']
    return redirect('/login/',)