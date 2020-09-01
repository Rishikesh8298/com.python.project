from __future__ import unicode_literals
from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    uname = models.CharField(max_length=50)

    def __str__(self):
        return self.name
