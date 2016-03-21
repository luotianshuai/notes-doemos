#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
import re
from django.core.exceptions import ValidationError

#定义登录表单样式
class LoginForm(forms.Form):
    username = forms.EmailField(
        error_messages={'required':u'邮箱账户不能为空'},
        widget=forms.widgets.EmailInput(attrs={'class': "form-control", "placeholder":"邮箱"})
    )
    password = forms.CharField(error_messages={'required':u'密码不能为空'},
        widget=forms.widgets.PasswordInput(attrs={'class': "form-control", "placeholder":"密码"})
    )



def ip_validate(value):
    ip_re = re.compile(r'^([0-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.([0-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.([0-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.([0-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$')
    if not ip_re.match(value):
        raise ValidationError('IP格式错误')



class  HostAdd(forms.Form):
        host_business_choice = (
        (1, u'大保健'),
        (2, u'喜乐街'),)
        host_business = forms.IntegerField(widget=forms.widgets.Select(choices=host_business_choice,attrs={'class':'form-control no-radius'}))

        host_status_choice = (
        (1, u'上线'),
        (2, u'下线'),)
        host_status = forms.IntegerField(widget=forms.widgets.Select(choices=host_status_choice,attrs={'class':'form-control no-radius'}))

        host_ip = forms.CharField(validators=[ip_validate, ],
                            error_messages={'required': u'IP不能为空'},
                            widget=forms.TextInput(attrs={'class': "form-control no-radius",
                                                          'placeholder': u'IP地址'}))


        host_port = forms.CharField(error_messages={'required':u'端口不能为空'},
                                    widget=forms.TextInput(attrs={'class': "form-control no-radius",
                                                          'placeholder': u'主机端口'}))

        host_id = forms.CharField(error_messages={'required':u'ID不能为空'},
                                  widget=forms.TextInput(attrs={'class': "form-control no-radius",
                                                          'placeholder': u'主机唯一ID'}))
        host_name = forms.CharField(error_messages={'required':u'主机名不能为空'},
                                  widget=forms.TextInput(attrs={'class': "form-control no-radius",
                                                          'placeholder': u'主机名'}))
