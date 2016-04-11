#/usr/bin/env python
#-*- coding:utf-8 -*-

from django.shortcuts import render
import models
# Create your views here.

class Pager(object):
    def __init__(self,current_page):
        self.current_page = int(current_page)
    @property
    def start(self):
        return (self.current_page-1) * 10

    @property
    def end(self):
        return self.current_page * 10

    def page_str(self,all_item,base_url):
        all_page,div = divmod(all_item,10)
        if div>0:
            all_page +=1
        pager_list = []
        # pager_str = ""
        # #默认用户可能看到的页码11个
        # start = self.current_page - 5
        # end = self.current_page + 6
        # for i in range(start,end):
        #     if i  == self.current_page:
        #         temp = '<a style="color:red;font-size:26px;" href="%s%d">%d</a>' % (base_url,i,i)
        #     else:
        #         temp = '<a href="%s%d">%d</a>' % (base_url,i,i)
        #     pager_str += temp

        if all_page <=1:
            start = 1
            end = all_page
        else:
            if self.current_page<=6:
                start = 1
                end =12
            else:
                start = self.current_page - 5
                end = self.current_page + 6
                if self.current_page+6 > all_page:
                    start = all_page - 11
                    end = all_page + 1
        for i in range(start,end):
            if i == self.current_page:
                temp = '<a style="color:red;font-size:26px;" href="%s%d">%d</a>' % (base_url,i,i)
            else:
                temp = '<a href="%s%d">%d</a>' % (base_url,i,i)
            pager_list.append(temp)
        #上一页
        if self.current_page >1:
            pre_page = '<a href="%s%d">上一页</a>' %(base_url,self.current_page - 1)
        else:
            pre_page = '<a href="javascript:void(0);">上一页</a>'
        if self.current_page >= all_page:
            next_page = '<a href="javascript:void(0);">下一页</a>'
        else:
            next_page = '<a href="%s%d">下一页</a>' %(base_url,self.current_page + 1)

        pager_list.insert(0,pre_page)
        pager_list.append(next_page)


        return "".join(pager_list)

def user_list(request):
    # for item in range(101,500):
    #     temp = {'username':'name%d' % item,'age':item}
    #     models.UserList.objects.create(**temp)
    # print models.UserList.objects.all().count()


    # current_page = request.GET.get('page',1)
    # current_page = int(current_page)
    # start = (current_page - 1)*10  # 10 20 (current_page-1)*10
    # end = current_page * 10 #20 30 current_page*10
    # result = models.UserList.objects.all()[start:end]

    current_page = request.GET.get('page',1)
    page_obj = Pager(current_page)
    result = models.UserList.objects.all()[page_obj.start:page_obj.end]
    #每页显示10条数据
    #共100条数据
    all_item = models.UserList.objects.all().count()
    pager_str = page_obj.page_str(all_item,"/user_list/?page=")

    return render(request,'user_list.html',{'result':result,'pager_str':pager_str})














