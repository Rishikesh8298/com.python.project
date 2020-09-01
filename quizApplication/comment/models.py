from __future__ import unicode_literals
from django.db import models

class Comment(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70)
    message=models.TextField()

    def __str__(self):
        return self.name

