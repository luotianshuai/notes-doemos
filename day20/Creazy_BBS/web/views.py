#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.shortcuts import render
import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import HttpResponseRedirect
from forms import ArticleForm
from tools import handle_upload_file


# Create your views here.

def index(request):
    articles = models.Article.objects.all()
    return render(request,'index.html',{'articles':articles})


def category(request,category_id):
    articles = models.Article.objects.filter(category_id=category_id)
    return render(request,'index.html',{'articles':articles})


def article_detaill(request,article_id):
    if request.method == "POST":
        pass
    try:
        article_obj = models.Article.objects.get(id=article_id)
    except ObjectDoesNotExist as e:
        return render(request,'404.html',{'error_msg':u'文章不存在'})
    return render(request,'article.html',{'article_obj':article_obj})


def acount_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def acount_login(request):
    articles = models.Article.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        #如果验证成功就是这个user对象
        if user is not None:
            login(request,user)
            return render(request,'index.html',{'articles':articles})
    return render(request,'index.html',{'articles':articles,})


def new_article(request):
    category_list = models.Category.objects.all()
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['author_id'] = request.user.userprofile.id

            #自定义图片上传
            new_img_path = handle_upload_file(request.FILES['head_img'],request)
            #但是在views也保存了一份,我们给他改掉改成我们自己的就行了
            form_data['head_img'] = new_img_path



            #create只能返回成功失败,我想在创建完成之后返回文章的ID,直接下面那么写就可以
            print form_data
            new_article_obj = models.Article(**form_data)
            new_article_obj.save()#这个对象就直接返回了
            return render(request,'new_article.html',{'new_article_obj':new_article_obj}) #如果没有这个变量说明是创建新文章呢
        else:
            print form.errors

    return render(request,'new_article.html',{'category_list':category_list})



