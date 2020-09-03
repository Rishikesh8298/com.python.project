from django.shortcuts import render, redirect, get_object_or_404
from main.models import Main
from question.models import Question
from .models import Record

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

    return render(request, "front/user/record_list_user.html")
