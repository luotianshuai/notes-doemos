import random
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
# Create your views here.


class MyView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        context['now'] = 'hello'
        context['test'] = [random.randint(1, 100) for i in range(100)]
        return context

    def get(self, request, *args, **kwargs):
        # view logic
        context = self.get_context_data()
        return render(request, self.template_name, context)


class GettingView(View):
    getting = 'Good Day'

    def get(self, request):
        # view logic
        return HttpResponse(self.getting)


class MorningGreetingView(GettingView):
    getting = 'Morning Day'

    def get(self, request):
        # view logic
        return HttpResponse(self.getting)
