#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Tim Luo  LuoTianShuai

from django.shortcuts import render
from app01.forms import home as HomeForm
from app01 import models
from django.db.models import Count,Min,Max,Sum

def index(request):
    obj = HomeForm.ImportForm(request.POST)
    val = request.GET.get('usertype')
    host_list = models.Host.objects.filter(user_group__user_type__typelist=val)
    if request.method == 'POST':
        if obj.is_valid():
            data = obj.clean()
            '''
            #两种方式
            #第一种方式先获取对象,通过对象的方式添加!
            grop_obj = models.UserGroup.objects.get(id=data['group'])
            print grop_obj
            models.Host.objects.create(hostname=data['hostname'],
                                       ip=data['ip'],
                                       user_group=grop_obj)
                                       #这里需要注意group_obj是一个对象原因如下:
            [在Model里咱们的user_group = user_group = models.ForeignKey('UserGroup') 这里他对应了一个对象,所以我们添加的时候添加对象即可]
            '''
            print data
            #第二种方式就简单了
            models.Host.objects.create(hostname=data['hostname'],
                                       ip=data['ip'],
                                       user_group_id=data['group'])
                                       #因为在存储的时候Django后默认在ForeignKey后面加一个_id所以我们给他加一个_id就可以直接添加了


        return render(request,'home/index.html',{'obj':obj,'host_list':host_list})
    return render(request,'home/index.html',{'obj':obj,'host_list':host_list})


def upload(request):
    if request.method == "POST":
        inp_file = request.FILES
        file_obj1 = inp_file.get('f1')
        print file_obj1.name


        #打开一个文件
        f = open(file_obj1.name,'wb')
        for line in file_obj1.chunks():
            f.write(line)
        f.close()
    return render(request,'home/upload.html')











