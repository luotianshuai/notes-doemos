#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
import re
from django.core.exceptions import ValidationError
from cmdb import models


def ip_validate(value):
    ip_re = re.compile(r'^([0-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.([0-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.([0-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.([0-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$')
    if not ip_re.match(value):
        raise ValidationError('IP格式错误')



class  HostAdd(forms.Form):
        def __init__(self,*arg,**kwargs):
            super(HostAdd,self).__init__(*arg,**kwargs)
            self.fields['hoststatus'].widget.choices = models.HostStatus.objects.all().values_list('id','hoststatus')
            self.fields['hostbusiness'].widget.choices = models.HostBusiness.objects.all().values_list('id','hostbusiness')
            self.fields['groupname'].widget.choices = models.Gorup.objects.all().values_list('id','groupname')


        hoststatus = forms.IntegerField(widget=forms.widgets.Select())
        hostbusiness = forms.IntegerField(widget=forms.widgets.Select())
        groupname = forms.IntegerField(widget=forms.widgets.Select())
        hostip_re = forms.GenericIPAddressField()

        hostip = forms.CharField(validators=[ip_validate, ],
                            error_messages={'required': u'IP不能为空'},
                            widget=forms.TextInput(attrs={'class': "form-control no-radius",
                                                          'placeholder': u'IP地址不能重复'}))


        hostport = forms.CharField(error_messages={'required':u'端口不能为空'},
                                    widget=forms.TextInput(attrs={'class': "form-control no-radius",
                                                          'placeholder': u'主机端口'}))

        hostname = forms.CharField(error_messages={'required':u'主机名不能为空'},
                                  widget=forms.TextInput(attrs={'class': "form-control no-radius",
                                                          'placeholder': u'主机名不能重复'}))
