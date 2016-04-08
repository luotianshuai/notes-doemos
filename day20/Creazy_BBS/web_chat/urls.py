"""Creazy_BBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard,name='web_chat'),
    url(r'^contacts/$', views.contacts,name='load_contact_list'),
    url(r'^msg/$', views.new_msg,name='send_msg'),
    url(r'^msg/$', views.new_msg,name='get_new_msg'),
    url(r'^userstatus/$', views.change_status,name='change_user_status'),

]
