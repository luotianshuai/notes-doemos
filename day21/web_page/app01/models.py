from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserList(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
