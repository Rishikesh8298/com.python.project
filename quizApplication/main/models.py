from __future__ import unicode_literals
from django.db import models

class Main(models.Model):
    name= models.CharField(max_length=50, default="Online")
    email=models.CharField(max_length=50, default="-")
    phone=models.CharField(max_length=13, default="-" )
    youtube=models.CharField(max_length=50, default="#" )
    facebook=models.CharField(max_length=50, default="#" )
    twitter=models.CharField(max_length=50, default="#" )
    about=models.TextField(default="-")
    aboutAdmin = models.TextField(default="-")
    set_name=models.CharField(max_length=50, default="#")

    def __str__(self):
        return self.set_name
