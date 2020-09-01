from django.shortcuts import render, redirect, get_object_or_404
from main.models import Main
from question.models import Question
from .models import Subject

def subject_add(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    if request.method=="POST":
        subject=request.POST.get("subject")
        if subject=="":
            error="Subject are Required"
            return render(request, 'back/error.html', {"error":error})
        if len(Subject.objects.filter(subject=subject)) != 0:
            error="This Subject used before"
            return render(request, 'back/error.html', {"error":error})
        data=Subject(subject=subject)
        data.save()
        return redirect("subject_list")
    return render(request, "back/subject_add.html")

def subject_list(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    sub=Subject.objects.all()
    return render(request, "back/subject_list.html", {"sub":sub})