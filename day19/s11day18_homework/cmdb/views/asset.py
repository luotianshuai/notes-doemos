# coding:utf-8
from django.shortcuts import render
from cmdb.forms import asset as AssetForm
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from cmdb import models
from backend.decorators.login_auth import login_auth
import json

# Create your views here.



#资产页面&用户页面
@login_auth
def lists(request):
    username = request.session['auth_user']
    host_info = models.HostInfo.objects.all()
    return render(request, 'asset/lists.html',{'username':username,'hostinfo_list':host_info,})

@login_auth
def get_select(request):
    ret = {'status':True,'error':'','status_list':[],'business_list':[]}
    for i in models.HostStatus.objects.all():
        ret['status_list'].append({'id':i.id,'text':i.hoststatus})
    for j in models.HostBusiness.objects.all():
        ret['business_list'].append({'id':j.id,'text':j.hostbusiness})

    ret = json.dumps(ret)
    print ret
    return HttpResponse(ret)

#用户通过ajax进行数据保存
@login_auth
def save_hostinfo(request):
    host_info = models.HostInfo.objects.all()
    user_post = json.loads(request.POST['data'])

    ret = {'status':True,'error':'','change_count':0}
    try:
        for i in user_post:
            change = False
            host_key = host_info.get(id=i['host_id'])
            # #test 就是这一条，数据库的对象，使用host_id = i['host_id']来进行匹配
            # #找到这个ID，然后循环i判断值是否变更，如果变更增加变更记录（增加到状态中）
            if host_key.hostname != i['host_name']:
                models.HostInfo.objects.filter(id=i['host_id']).update(hostname=i['host_name'],
                                                                      hostport=i['host_port'],
                                                                      hostip=i['host_ip'],
                                                                      hoststatus_id=i['host_status'],
                                                                      hostbusiness_id=i['host_business'],
                                                                      )
                change = True
            if host_key.hostip != i['host_ip']:
                models.HostInfo.objects.filter(id=i['host_id']).update(hostname=i['host_name'],
                                                                      hostport=i['host_port'],
                                                                      hostip=i['host_ip'],
                                                                      hoststatus_id=i['host_status'],
                                                                      hostbusiness_id=i['host_business'],
                                                                      )
                change = True
            if host_key.hostport != i['host_port']:
                models.HostInfo.objects.filter(id=i['host_id']).update(hostname=i['host_name'],
                                                                      hostport=i['host_port'],
                                                                      hostip=i['host_ip'],
                                                                      hoststatus_id=i['host_status'],
                                                                      hostbusiness_id=i['host_business'],
                                                                      )
                change = True
            if host_key.hostbusiness_id != int(i['host_business']):
                models.HostInfo.objects.filter(id=i['host_id']).update(hostname=i['host_name'],
                                                                      hostport=i['host_port'],
                                                                      hostip=i['host_ip'],
                                                                      hoststatus_id=i['host_status'],
                                                                      hostbusiness_id=i['host_business'],
                                                                      )
                change = True
            if host_key.hoststatus_id != int(i['host_status']):
                models.HostInfo.objects.filter(id=i['host_id']).update(hostname=i['host_name'],
                                                                      hostport=i['host_port'],
                                                                      hostip=i['host_ip'],
                                                                      hoststatus_id=i['host_status'],
                                                                      hostbusiness_id=i['host_business'],
                                                                      )
                change = True
            if change:
                ret['change_count'] += 1
    except Exception,e:
            ret['status'] = False
            ret['error'] = str(e)

    return HttpResponse(json.dumps(ret))




#用户添加数据(优化添加)
@login_auth
def add(request):
    user_input = AssetForm.HostAdd(request.POST)
    if request.method == 'POST' :
        if user_input.is_valid():
            data = user_input.clean()
            print data
            if models.HostInfo.objects.filter(hostname=data['hostname']):
                return render(request,'asset/import_single.html',{'model':user_input,'check':'主机名已存在请修改主机名',})
            elif models.HostInfo.objects.filter(hostip=data['hostip']):
                return render(request,'asset/import_single.html',{'model':user_input,'check':'IP地址存在请修改主机名',})

            else:
                models.HostInfo.objects.create(hostip=data['hostip'],hostname=data['hostname'],hostport=data['hostport'],
                                               group_id=data['groupname'],hostbusiness_id=data['hostbusiness'],
                                               hoststatus_id=data['hoststatus'],
                                              )
                return render(request,'asset/import_single.html',{'model':user_input,'succeed':'主机已添加',})
        else:
            error_msg = user_input.errors.as_data()
            return render(request,'asset/import_single.html',{'model':user_input,'message':error_msg,})

    return render(request, 'asset/import_single.html',{'model':user_input,})


#用户删除数据,通过模态对话框
@login_auth
def del_hostinfo(request):
    user_post = json.loads(request.POST['data'])
    ret = {'status':True,'error':'','change_count':0}
    print user_post

    for i in user_post:
        models.HostInfo.objects.filter(id=i).delete()
        ret['change_count'] += 1
    return HttpResponse(json.dumps(ret))
