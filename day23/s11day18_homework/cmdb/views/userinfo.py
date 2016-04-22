# coding:utf-8
from django.shortcuts import render
from backend.decorators.login_auth import login_auth

# Create your views here.

@login_auth
def user(request):
    return render(request,'userinfo/user.html')