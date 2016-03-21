# coding:utf-8
from django.shortcuts import render
from cmdb import forms
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from cmdb import models
from backend.decorators.login_auth import login_auth
import json

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

@login_auth
def save_hostinfo(request):
    host_info = models.HostInfo.objects.all()
    user_post = json.loads(request.POST['data'])

    #print host_info.get(host_id=1).host_id

    ret = {'status':True,'error':'','change_count':0}
    try:
        for i in user_post:
            change = False
            #test 就是这一条，数据库的对象，使用host_id = i['host_id']来进行匹配
            #找到这个ID，然后循环i判断值是否变更，如果变更增加变更记录（增加到状态中）
            test = host_info.get(host_id=i['host_id'])
            if i['host_name'] != test.host_name:
                test.host_name = i['host_name']
                change = True
            if i['host_port'] != test.host_port:
                test.host_port = i['host_port']
                change = True
            if i['host_ip'] != test.host_ip:
                test.host_ip = i['host_ip']
                change = True
            if i['host_business'] != test.host_business:
                test.host_business = i['host_business']
                change = True
            if i['host_status'] != test.host_status:
                test.host_status = i['host_status']
                change = True
            if change:
                ret['change_count'] += 1
            test.save()
    except Exception,e:
            ret['status'] = False
            ret['error'] = str(e)

    return HttpResponse(json.dumps(ret))





@login_auth
def add(request):
    obj = forms.HostAdd()
    if request.method == 'POST':
        user_input = forms.HostAdd(request.POST)
        if user_input.is_valid():
            data = user_input.clean()
            host_info = models.HostInfo.objects.all()
            if models.HostInfo.objects.filter(host_id=data['host_id']):
                return render(request,'asset/import_single.html',{'model':obj,'check':'主机唯一ID已存在请修改主机ID',})
            else:
                models.HostInfo.objects.create(host_id=data['host_id'],host_port=data['host_port'],host_ip=data['host_ip'],
                                              host_business=data['host_business'],host_status=data['host_status'],
                                              host_name=data['host_name']
                                              )
                return render(request,'asset/import_single.html',{'model':obj,'succeed':'主机已添加',})

        else:
            error_msg = user_input.errors.as_data()
            return render(request,'asset/import_single.html',{'model':obj,'message':error_msg,})

    return render(request, 'asset/import_single.html',{'model':obj,})

@login_auth
def del_hostinfo(request):
    host_info = models.HostInfo.objects.all()
    user_post = json.loads(request.POST['data'])
    #print host_info.get(host_id=1).host_id
    ret = {'status':True,'error':'','change_count':0}
    print user_post

    for i in user_post:
        models.HostInfo.objects.filter(host_id=i).delete()
        ret['change_count'] += 1
        return HttpResponse(json.dumps(ret))
def logout(request):
    del request.session['auth_user']
    return redirect('/login/')