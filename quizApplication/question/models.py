from __future__ import unicode_literals
from django.db import models

class Question(models.Model):
    subject=models.CharField(max_length=30, default="Python(Static)")
    questionName= models.TextField()
    option1=models.CharField(max_length=150)
    option2=models.CharField(max_length=150)
    option3=models.CharField(max_length=150)
    option4=models.CharField(max_length=150)
    answer=models.CharField(max_length=150)