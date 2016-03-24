#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Tim Luo  LuoTianShuai


from django import forms
from app01 import models
import json


class ImportForm(forms.Form):
    def __init__(self,*arg,**kwargs):
        super(ImportForm,self).__init__(*arg,**kwargs)
        self.fields['group'].widget.choices = models.UserGroup.objects.all().values_list('id','caption')

    group = forms.CharField(
        widget=forms.Select()
    )
    hostname = forms.CharField()
    ip = forms.GenericIPAddressField()


# class ImportForm(forms.Form):
#     HOST_TYPE_LIST = (
#         (1,'物理机'),
#         (2,'虚拟机'),
#     )
#
#     host = forms.IntegerField(
#         widget=forms.Select(choices=HOST_TYPE_LIST)
#     )

#
# class ImportForm(forms.Form):
#     f = open('db_admin')
#     data = f.read()
#     data_tuple = json.loads(data)
#     f.close()
#     host = forms.IntegerField(
#         widget=forms.Select(choices=data_tuple)
#     )
#
#     def __init__(self, *args, **kwargs):
#         super(ImportForm, self).__init__(*args, **kwargs)
#         f = open('db_admin')
#         data = f.read()
#         data_tuple = json.loads(data)
#         f.close()
#
#         #通过self.fields找到host这个静态字段的.wideget.choices属性并重新给他赋值!
#         self.fields['host'].widget.choices = data_tuple
#
#
#




