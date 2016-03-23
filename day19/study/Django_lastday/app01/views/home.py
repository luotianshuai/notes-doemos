#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Tim Luo  LuoTianShuai

from django.shortcuts import render
from app01.forms import home as HomeForm
from app01 import models

def index(request):
    test = models.UserInfo.objects.filter(username='dashuaige')
    print test

    obj = HomeForm.ImportForm(request.POST)
    return render(request,'home/index.html',{'obj':obj})


def upload(request):
    if request.method == "POST":
        inp_post = request.POST
        inp_file = request.FILES
        file_obj1 = inp_file.get('f1')
        print file_obj1.name

        #打开一个文件
        f = open(file_obj1.name,'wb')
        for line in file_obj1.chunks():
            f.write(line)
        f.close()
    return render(request,'home/upload.html')











