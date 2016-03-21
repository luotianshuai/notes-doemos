#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Tim Luo  LuoTianShuai


from django import forms
from app01 import models
import json


class ImportForm(forms.Form):
    def __init__(self,*arg,**kwargs):
        super(ImportForm,self).__init__(*arg,**kwargs)
    #     # f = open('db_admin')
    #     # data = f.read()
    #     # data_tuple = json.loads(data)
    #
    #     self.fields['admin'].widget.choices = data_tuple
    #
    # fr = open('db_admin')
    # data = fr.read()
    # data_tuple = json.loads(data)
        self.fields['admin'].widget.choices = models.SimpleModel.objects.all().values_list('id','username')

    admin = forms.IntegerField(
        widget=forms.Select()
    )