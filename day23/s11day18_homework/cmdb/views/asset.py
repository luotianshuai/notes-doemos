# coding:utf-8
from django.shortcuts import render
from cmdb.forms import asset as AssetForm
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.db.models import Q
from cmdb import models
from backend.decorators.login_auth import login_auth
import json
from django.utils.safestring import mark_safe

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


@login_auth
def search_info(request):
    #获取用户请求的数据
    user_post = json.loads(request.GET['search_list'])
    print user_post
    #生成搜索对象
    Serach_Q = Q()
    #循环字典并生成搜索条件集合
    for k,v in user_post.items():
        #生成一个搜索结合
        q = Q()
        #生命集合中的搜索条件为'或'条件
        q.connector = 'OR'
        #循环字典中的value,value是前端传过来的条件集合
        for i in v:
            #在搜索条件集合中增加条件,条件为元组形式,k为字典中的key! key是字段名或者跨表字段名或者支持_gt等
            #i为字典中的vlaue中的元素,为条件
            #
            q.children.append((k,i))
        #没循环一次后后,吧他加入到总的搜索条件中
        Serach_Q.add(q,'AND')
    #使用总的搜索条件进行查询
    data = models.HostInfo.objects.filter(Serach_Q)
    #拼接字符串并返回
    html = []
    for i in data:
        html.append(
            "<tr>"+
                "<td>" + "<input type='checkbox' >"+ "</td>" +
                "<td name='host_id'>" + '%s' %i.id + "</td>" +
                "<td name='host_name' edit='true'>" + i.hostname + "</td>"+
                "<td name='host_ip' edit='true'>" + i.hostip + "</td>"+
                "<td name='host_port' edit='true'>" + '%s' %i.hostport + "</td>"+
                "<td name='host_business' edit='true' edit-type='select' global-key='BUSINESS' select-val='" + '%s' %i.hostbusiness_id + "'>" + i.hostbusiness.hostbusiness + "</td>"+
                "<td name='host_status' edit='true' edit-type='select' global-key='STATUS' select-val='" + '%s' %i.hoststatus_id + "'>" + i.hoststatus.hoststatus + "</td>"+
            "</tr>"
        )

    html = mark_safe("".join(html))
    return HttpResponse(html)
