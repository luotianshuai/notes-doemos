#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
       widget=forms.widgets.TextInput(attrs={'class': "form-control", "placeholder":"用户名"})
    )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={'class': "form-control", "placeholder":"密码"})
    )