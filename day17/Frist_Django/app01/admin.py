#/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib import admin

# Register your models here.

#导入app01模块
from app01 import models

#注册咱们创建的类,通过他来访问
admin.site.register(models.UserInfo)
