from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment

def feedback(request):
    print("I'm in Feedback function")
    if request.method =="POST":
        print("I'm in Feedback function inseide if")
        name=request.POST.get("username")
        email=request.POST.get("email")
        message=request.POST.get("message")
        print(name, email, message)
        data=Comment(name=name, email=email, message=message)
        data.save()
    return redirect('about')

def comment_list(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    comment=Comment.objects.all()
    
    return render(request, "back/comment_list.html", {"comment": comment})
