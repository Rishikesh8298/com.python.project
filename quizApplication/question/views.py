from django.shortcuts import render, redirect
from .models import Question
from subject.models import Subject

def question_add(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    sub=Subject.objects.all()
    if request.method=="POST":
        subject=request.POST.get("subject")
        question=request.POST.get("question")
        option1=request.POST.get("option1")
        option2=request.POST.get("option2")
        option3=request.POST.get("option3")
        option4=request.POST.get("option4")
        answer=request.POST.get("answer")
        if option1=="" or option2=="" or question=="" or option3=="" or option4=="" or answer=="" or subject=="":
            error="All Fields are required!!"
            return render(request, "back/error.html", {"error": error})
        else:
            data=Question(subject=subject, questionName=question, option1=option1, option2=option2, option3=option3, option4=option4, answer=answer)
            data.save()

            count=len(Question.objects.filter(subject=subject))
            b=Subject.objects.get(subject=subject)
            b.count=count
            b.save()

            return redirect('question_list')
    return render(request, "back/question_add.html", {"sub":sub})

def question_list(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    question=Question.objects.all()
    return render(request, 'back/question_list.html', {"question": question})

def question_delete(request, pk):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    try:
        b=Question.objects.get(pk=pk)
        subject = b.subject
        b.delete()

        count=len(Question.objects.filter(subject=subject))
        data=Subject.objects.get(subject=subject)
        data.count=count
        data.save()
    except:
        error="Something Wrong Happend!!"
        return render(request, "back/error.html", {"error": error})
    return redirect("question_list")

def question_edit(request, pk):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    question=Question.objects.get(pk=pk)
    sub=Subject.objects.all()
    
    if len(Question.objects.filter(pk=pk))==0:
        error="Question ID not found!!"
        return render(request, 'back/error.html', {"error":error})

    
    if request.method=="POST":
        subject=request.POST.get("subject")
        question=request.POST.get("question")
        option1=request.POST.get("option1")
        option2=request.POST.get("option2")
        option3=request.POST.get("option3")
        option4=request.POST.get("option4")
        answer=request.POST.get("answer")
        if option1=="" or option2=="" or question=="" or option3=="" or option4=="" or answer=="" or subject=="":
            error="All Fields are required!!"
            return render(request, "back/error.html", {"error": error})
        else:
            data=Question.objects.get(pk=pk)
            data.subject=subject
            data.questionName=question
            data.option1=option1
            data.option2=option2
            data.option3=option3
            data.option4=option4
            data.answer=answer
            data.save()
            return redirect('question_list')
    return render(request, "back/question_edit.html", {"pk":pk, "question":question, "sub":sub})
