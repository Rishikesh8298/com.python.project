from __future__ import unicode_literals
from django.db import models

class Subject(models.Model):
    subject=models.CharField(max_length=20)
    count=models.IntegerField(default=0)    

    def __str__(self):
        return self.subject
    
    