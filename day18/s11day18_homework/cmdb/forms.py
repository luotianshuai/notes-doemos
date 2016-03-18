#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms


#定义登录表单样式
class LoginForm(forms.Form):
    username = forms.EmailField(
        error_messages={'required':u'邮箱账户不能为空'},
        widget=forms.widgets.EmailInput(attrs={'class': "form-control", "placeholder":"邮箱"})
    )
    password = forms.CharField(error_messages={'required':u'密码不能为空'},
        widget=forms.widgets.PasswordInput(attrs={'class': "form-control", "placeholder":"密码"})
    )