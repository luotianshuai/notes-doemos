# coding:utf-8
from django.shortcuts import render
from backend.decorators.login_auth import login_auth

# Create your views here.

@login_auth
def index(request):
    username = request.session['auth_user']
    return render(request, 'home/index.html',{'username':username})
