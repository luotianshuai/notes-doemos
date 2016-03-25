from django.contrib import admin

# Register your models here.

from cmdb import models

admin.site.register(models.UserInfo)
admin.site.register(models.Gorup)
admin.site.register(models.HostStatus)
admin.site.register(models.HostBusiness)
admin.site.register(models.HostInfo)