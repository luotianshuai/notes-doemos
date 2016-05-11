from __future__ import unicode_literals

from django.db import models

# Create your models here.


class HostType(models.Model):
    hosttype = models.CharField(max_length=32)


