from __future__ import unicode_literals
from django.db import models

class Record(models.Model):

    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50, default="-")
    correctAnswer=models.CharField(max_length=20)
    totalQuestion=models.CharField(max_length=20)
    date=models.CharField(max_length=20, default="00/00/00")

    def __str__(self):
        return self.name