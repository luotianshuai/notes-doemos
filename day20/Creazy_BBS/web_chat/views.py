#/usr/bin/env python
#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from web_chat import models
#导入Django自带的判断用户是否登录的模块
from django.contrib.auth.decorators import login_required
# Create your views here.
import time
import json
import Queue
GLOBAL_MQ = {

}




#应用装饰器
@login_required
def dashboard(request):
    return render(request,'web_chat/dashboard.html')


@login_required
def contacts(request):
    contact_dic = {}
    #通过一个字段去查多对多都要使用select_related
    contacts = request.user.userprofile.friends.select_related().values('id','name','status')
    contact_dic['contact_list']= list(contacts)
    groups = request.user.userprofile.qqgroup_set.select_related().values('id','name','max_member_nums')
    contact_dic['group_list'] = list(groups)
    print(contact_dic)
    return HttpResponse(json.dumps(contact_dic))



def new_msg(request):
    if request.method == 'POST':
        print request.POST.get('data')

        #获取用户发过来的数据
        data = json.loads(request.POST.get('data'))
        send_to = data['to']
        #判断队列里是否有这个用户名,如果没有新建一个队列
        if send_to not in GLOBAL_MQ:
            GLOBAL_MQ[send_to] = Queue.Queue()
        data['timestamp'] = time.strftime("%Y-%m-%d %X", time.localtime())
        GLOBAL_MQ[send_to].put(data)

        return HttpResponse(GLOBAL_MQ[send_to].qsize())
    else:
        #因为队列里目前存的是字符串所以我们需要先给他转换为字符串
        request_user = str(request.user.userprofile.id)
        msg_lists = []
        #判断是否在队列里
        if request_user in GLOBAL_MQ:
            #判断有多少条消息
            stored_msg_nums = GLOBAL_MQ[request_user].qsize()
            #把消息循环加入到列表中并发送
            for i in range(stored_msg_nums):
                msg_lists.append(GLOBAL_MQ[request_user].get())
        return HttpResponse(json.dumps(msg_lists))