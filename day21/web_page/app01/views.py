#/usr/bin/env python
#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
import models
from paging import Pager


def user_list(request):
    current_page = request.GET.get('page',1)
    page_obj = Pager(current_page)
    #把方法改造成属性(2),这样在下面调用方法的时候就不需要加括号了
    result = models.UserList.objects.all()[page_obj.start:page_obj.end]
    all_item = models.UserList.objects.all().count()
    pager_str = page_obj.page_str(all_item,'/user_list/')

    return render(request,'user_list.html',{'result':result,'pager_str':pager_str})













