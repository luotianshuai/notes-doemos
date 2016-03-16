from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    print 'app01.index'
    return HttpResponse('OK')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')

        if username == 'tim' and pwd == '123':
            request.session['IS_LOGIN'] = True
            return redirect('/app01/home/')

    return render(request,'login.html')

def home(request):
    is_login = request.session.get('IS_LOGIN',False)
    if is_login:
        return HttpResponse('HOME')
    else:
        return redirect('/app01/login')


from django import forms
class UserInfo(forms.Form):
    email = forms.EmailField()
    host = forms.CharField()
    port = forms.CharField()
    mobile = forms.CharField()

def user_list(request):
    obj = UserInfo()

    if request.method == 'POST':
        user_input_obj = UserInfo(request.POST)
        if user_input_obj.is_valid():
            data = user_input_obj.clean()
            print data
        else:
            error_msg = user_input_obj.errors
            return render(request,'user_info_list.html',{'obj':obj,'error':error_msg})
    return render(request,'user_info_list.html',{'obj':obj,})

def ajax_data(request):
    print request.POST
    return HttpResponse('OK')