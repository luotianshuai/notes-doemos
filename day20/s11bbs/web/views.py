from django.shortcuts import render
import models
# Create your views here.


def index(request):
    articles = models.Article.objects.all()
    return render(request,'index.html',{'articles':articles})


def category(request,category_id):
    articles = models.Article.objects.filter(categroy_id=category_id)
    return render(request,'index.html',{'articles':articles})


def test(request):
    return render(request,'childe.html')