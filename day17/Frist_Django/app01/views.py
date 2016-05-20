#/usr/bin/env python
#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from app01 import models
import hashlib
#Django 在返回的时候需要一层封装,需要导入HttpResponse
from django.shortcuts import HttpResponse
import time
# Create your views here.




from django.views.decorators.cache import cache_page

#这里设置的是 60秒 * 15 ,15分钟之后
@cache_page(60 * 15)
def cache_page(request):
    current = str(time.time())
    return HttpResponse(current)



def login(request):
    #如果是GET请求
    #如果是POST,检查用户输入
    #print request.method 来查看用户是通过什么方式请求的
    #还有个问题:当你POST的时候,会出现问题,现在临时解决方法是:在seetings里注释掉
    '''
    MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',  注释掉这一行
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    '''
    if request.method == 'POST':
        if request.method== 'POST' and request.POST.has_key('check_status'):
            print 'fuck you'
            input_addem = request.POST['email']
            user_info_list = models.UserInfo.objects.all()
            for i in user_info_list:
                if input_addem == i.email:
                    return HttpResponse('yes')
            else:
                return HttpResponse('no')

        #判断是否为登录请求
        elif request.POST.has_key('login'):
            input_email = request.POST['email']
            input_pwd = request.POST['pwd']
            lhash = hashlib.md5()
            lhash.update(input_pwd)
            input_pwd = lhash.hexdigest()
            user_info_list = models.UserInfo.objects.all()
            for i in user_info_list:
                print i.email
                print i.pwd
                if input_email == i.email and input_pwd == i.pwd:
                #当登录成功后给它跳转,这里需要一个模块from django.shortcuts import redirect
                #成功后跳转到指定网址
                    return redirect('/index/')
            else:
                #如果没有成功,需要在页面告诉用户用户名和密码错误.
                return render(request,'login.html',{'status':'用户名或密码错误'})
                #通过模板语言,来在login.html中添加一个status的替换告诉用户<span>{{ status }}</span>
        else:
            input_email = request.POST['email']
            input_pwd = request.POST['pwd']
            hash = hashlib.md5()
            hash.update(input_pwd)
            input_pwd = hash.hexdigest()
            print input_pwd
            models.UserInfo.objects.create(email=input_email,pwd=input_pwd) #他就表示去创建一条数据



    return render(request,'login.html')

def index(request):
    #数据库去数据
    #数据和HTML渲染
    #如果想使用数据库,需要先导入(需要在开头导入)
    if request.method =='POST':
        #获取UserInfo表中的数据,下面一行语句是固定搭配
        user_info_list = models.UserInfo.objects.all()
        #user_info 列表,列表的元素就是一行.每一行有两个字段:一个是email 一个pwd
        return render(request,'index.html',{'user_info_list':user_info_list},)
    else:
        user_info_list = models.UserInfo.objects.all()
        return render(request,'index.html',{'user_info_list':user_info_list},)

def deluser(request):
    if request.method == 'POST':
        input_em = request.POST['em']
        #判断是否有这个用户

        user_info_list = models.UserInfo.objects.all()
        for i in user_info_list:
            print i.email
            print i.pwd
            if input_em == i.email:
                models.UserInfo.objects.filter(email=input_em).delete() #找到email=input_em的数据并删除
                user_info_list = models.UserInfo.objects.all()
                return render(request,'deluser.html',{'user_info_list':user_info_list,'status':'删除成功'},)
        else:
            return render(request,'deluser.html',{'status':'无效用户','user_info_list':user_info_list},)
    else:
        user_info_list = models.UserInfo.objects.all()
        return render(request,'deluser.html',{'user_info_list':user_info_list},)

def change(request):
    if request.method == 'POST':
        input_changeem = request.POST['em']
        input_changepw = request.POST['pw']
        hash = hashlib.md5()
        hash.update(input_changepw)
        input_changepw = hash.hexdigest()
        #判断用户名是否存在
        user_info_list = models.UserInfo.objects.all()
        for i in user_info_list:
            print i.email
            print i.pwd
            if input_changeem == i.email:
                models.UserInfo.objects.filter(email=input_changeem,pwd=input_changepw)
                user_info_list = models.UserInfo.objects.all()
                return render(request,'change.html',{'user_info_list':user_info_list,'status':'修改成功'},)
        else:
            return render(request,'change.html',{'status':'无效用户','user_info_list':user_info_list},)
    else:
        user_info_list = models.UserInfo.objects.all()
        return render(request,'change.html',{'user_info_list':user_info_list},)


def adduser(request):
    if request.method== 'POST' and request.POST.has_key('check_status'):
            print 'fuck you'
            input_addem = request.POST['em']
            user_info_list = models.UserInfo.objects.all()
            for i in user_info_list:
                if input_addem == i.email:
                    return HttpResponse('yes')
            else:
                return HttpResponse('no')
    elif request.method == 'POST':
            input_addem = request.POST['em']
            input_addpw = request.POST['pw']
            hash = hashlib.md5()
            hash.update(input_addpw)
            input_changepw = hash.hexdigest()
            #判断用户名是否存在
            user_info_list = models.UserInfo.objects.all()
            for i in user_info_list:
                if input_addem == i.email:
                    return render(request,'adduser.html',{'user_info_list':user_info_list,'status':'用户已存在'},)
                else:
                     models.UserInfo.objects.create(email=input_addem,pwd=input_addpw) #他就表示去创建一条数据
                     user_info_list = models.UserInfo.objects.all()
                     return render(request,'adduser.html',{'user_info_list':user_info_list},)
    else:
        user_info_list = models.UserInfo.objects.all()
        return render(request,'adduser.html',{'user_info_list':user_info_list},)


def moreuser(request):
    if request.method == 'POST':
        moreuser_info = request.POST['moreadd']
        user_info = moreuser_info.split(',')
        print user_info
        for i in user_info:
            user_np = i.split(':')
            user_info_list = models.UserInfo.objects.all()
            for c in user_info_list:
                if user_np[0] == c.email:
                    return render(request,'moreuser.html',{'user_info_list':user_info_list,'user_check':user_np[0],'status':'用户名已存在:'},)
        else:
            for i in user_info:
                user_np = i.split(':')
                models.UserInfo.objects.create(email=user_np[0],pwd=user_np[1]) #他就表示去创建一条数据
            user_info_list = models.UserInfo.objects.all()
            return render(request,'moreuser.html',{'user_info_list':user_info_list},)
    else:
        user_info_list = models.UserInfo.objects.all()
        return render(request,'moreuser.html',{'user_info_list':user_info_list},)