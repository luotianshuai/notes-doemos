from django.shortcuts import render
from django.shortcuts import render
from app01 import models
from app01 import forms

def index(request):
    # models.HostType.objects.create(hosttype='CEO')
    # models.HostType.objects.create(hosttype='CFO')
    # models.HostType.objects.create(hosttype='COO')
    obj = forms.HostType(request.POST)
    return render(request,'index.html',{'obj':obj})