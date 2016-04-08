#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Tim Luo  LuoTianShuai
import os

def handle_upload_file(f,request):  #f这里获取到文件句柄
    base_img_upload_path = 'static/Uploads'
    user_path = "%s/%s" % (base_img_upload_path,request.user.userprofile.id)
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    with open('%s/%s'% (user_path,f.name),'wb+') as destinations:
        for chunk in f.chunks():
            destinations.write(chunk)
        #为了防止用户传送图片进行冲突,我们为每个用户进行创建用户


    return "/static/Uploads/%s/%s" % (request.user.userprofile.id,f.name)