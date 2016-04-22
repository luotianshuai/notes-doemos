#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django import forms
from app01 import models

class HostType(forms.Form):
    def __init__(self, *arg, **kwargs):
        super(HostType, self).__init__(*arg, **kwargs)
        self.fields['form_hosttype'].widget.choices = models.HostType.objects.all().values_list('id','hosttype')
    form_hosttype = forms.IntegerField(widget=forms.widgets.Select())
