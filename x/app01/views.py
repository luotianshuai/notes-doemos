from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse
# Create your views here.


class MyView(View):
    def get(self, request):
        # view logic
        return HttpResponse('Hello World')


class GettingView(View):
    getting = 'Good Day'

    def get(self):
        # view logic
        return HttpResponse(self.getting)


class MorningGreetingView(GettingView):
    getting = 'Morning Day'

    def get(self):
        # view logic
        return HttpResponse(self.getting)
