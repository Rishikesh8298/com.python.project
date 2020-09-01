from django.shortcuts import render, redirect, get_object_or_404
from .models import Manager
from main.models import Main
from question.models import Question
from record.models import Record
from subject.models import Subject
import datetime
from random import shuffle
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def manager_list(request):

   manager = Manager.objects.all()
   return render(request, "back/manager_list.html", {"manager": manager})

def manager_del(request, pk):
   manager = Manager.objects.get(pk=pk)
   user = User.objects.filter(username = manager.uname)
   user.delete()

   manager.delete()

   return redirect("manager_list")
