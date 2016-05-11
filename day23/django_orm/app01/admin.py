from django.contrib import admin

# Register your models here.

from app01 import models

admin.site.register(models.MyUser)
admin.site.register(models.News)
admin.site.register(models.Favor)






