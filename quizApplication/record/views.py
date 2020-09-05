from django.shortcuts import render, redirect, get_object_or_404
from main.models import Main
from question.models import Question
from .models import Record
from manager.models import Manager
import datetime
from subject.models import Subject

def record_list(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    data=Record.objects.all()

    return render(request, 'back/record.html', {"data":data})

def record_delete(request, pk):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    try:
        b=Record.objects.get(pk=pk)
        b.delete()
    except:
        error="Something Wrong Happend!!"
        return render(request, "back/error.html", {"error": error})
    return redirect("record_list")

def record_list_user(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    uemail=Manager.objects.get(uname=request.user).email
    history = Record.objects.filter(email=uemail).order_by("-pk")
    sub = Subject.objects.all()

    return render(request, "front/user/record_list_user.html", {"history":history, "sub":sub})

def user_result(request, word):
    site=Main.objects.get(pk=1)
    now=datetime.datetime.now()
    year=now.year
    month=now.month
    day=now.day
    if len(str(day))==1:
        day="0"+str(day)
    if len(str(month))==1:
        month="0"+str(month)
    today=str(year)+"/"+str(month)+"/"+ str(day)
    ttime=str(now.hour)+":"+str(now.minute)+":"+str(now.second)
    print(ttime)
    if request.method=="POST":
        question=Question.objects.filter(subject=word)
        name=request.POST.get("name")
        email=request.POST.get("email")
        correct=0
        ques=0
        for i in question:
            if i.answer==request.POST.get("answer"+str(i.pk)):
                correct=correct+1
            ques=ques+1
        if ques < 10:
            ques = ques
        else:
            ques= 10
        data=Record(name=name, email=email, subject=word, correctAnswer=correct, totalQuestion=ques, date=today, time=ttime)
        data.save()
        return render(request, 'front/user/result.html', {"correct":correct, "ques":ques, "name":name, "email":email, "site": site})
    return redirect('record_list_user')
