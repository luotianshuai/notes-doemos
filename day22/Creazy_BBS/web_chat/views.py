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
    print request.user.userprofile.friends.select_related()
    print contacts
    contact_dic['contact_list']= list(contacts)
    groups = request.user.userprofile.qqgroup_set.select_related().values('id','name','max_member_nums')
    contact_dic['group_list'] = list(groups)
    print(contact_dic)
    return HttpResponse(json.dumps(contact_dic))


@login_required
def new_msg(request):
    if request.method == 'POST':
        print request.POST.get('data')

        #获取用户发过来的数据
        data = json.loads(request.POST.get('data'))
        send_to = data['to']
        msg_from = data['from']
        #获取是否为组聊天
        contact_type = data['contact_type']
        if contact_type == 'group_contact':
            #获取组ID
            group_obj = models.QQGroup.objects.get(id=send_to)
            #循环这个组的所有成员,给每一个人都发送一条消息
            for member in group_obj.members.select_related():
                # 判断队列里是否有这个用户名,如果没有新建一个队列
                if str(member.id) not in GLOBAL_MQ:
                    GLOBAL_MQ[str(member.id)] = Queue.Queue()
                data['timestamp'] = time.strftime("%Y-%m-%d %X", time.localtime())
                if str(member.id) != msg_from:
                    GLOBAL_MQ[str(member.id)].put(data)

        #判断队列里是否有这个用户名,如果没有新建一个队列
        else:
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
            try:
                #如果没有新消息
                if stored_msg_nums == 0:
                    print "\033[41;1m没有消息等待,15秒.....\033[0m"
                    msg_lists.append(GLOBAL_MQ[request_user].get(timeout=15))
                '''
                    如果队列里面有没有消息,get就会阻塞,等待有新消息之后会继续往下走,这里如果阻塞到这里了,等有新消息过来之后,把消息加入到
                    msg_lists中后,for循环还是不执行的因为,这个stored_msg_mums是在上面生成的变量下面for调用这个变量的时候他还是为0
                    等返回之后再取得时候,现在stored_msg_nums不是0了,就执行执行for循环了,然后发送数据
                '''
            except Exception as e:
                print ('error:',e)
                print "\033[43;1m等待已超时......15秒.....\033[0m"

            # 把消息循环加入到列表中并发送
            for i in range(stored_msg_nums):
                msg_lists.append(GLOBAL_MQ[request_user].get())
        else:
            #创建一个新队列给这个用户
            GLOBAL_MQ[str(request.user.userprofile.id)] = Queue.Queue()
        return HttpResponse(json.dumps(msg_lists))


def change_status(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        #判断用户发送过来的数据状态
        if data == 'offline':
            #获取所有的好友
            login_user_id = request.user.userprofile.id
            group_obj = models.QQGroup.objects.get(id=login_user_id)

            for member in group_obj.members.select_related():
                # 判断队列里是否有这个用户名,如果没有新建一个队列
                if str(member.id) not in GLOBAL_MQ:
                    GLOBAL_MQ[str(member.id)] = Queue.Queue()
                #增加时间戳
                data['timestamp'] = time.strftime("%Y-%m-%d %X", time.localtime())

                if str(member.id) != login_user_id:
                    GLOBAL_MQ[str(member.id)].put(data)

    return HttpResponse('ddd')