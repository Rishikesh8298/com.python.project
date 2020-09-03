from django.shortcuts import render, redirect, get_object_or_404
from .models import Main
from question.models import Question
from record.models import Record
from subject.models import Subject
from manager.models import Manager
import datetime
from random import shuffle
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def home(request):
    site=Main.objects.get(pk=1)
    sub=Subject.objects.all()
    question=Question.objects.all()
    return render(request, 'front/home.html', {"question": question, "sub": sub, "site": site})

def about(request):
    site=Main.objects.get(pk=1)
    sub=Subject.objects.all()
    question=Question.objects.all()
    return render(request, "front/about.html",{"question": question, "sub": sub, "site": site})

def mylogin(request):

    if request.method=="POST":
        uname=request.POST.get("username")
        upass=request.POST.get("password")
        if uname != "" and upass != "":
            userlog = authenticate(username=uname, password=upass)
            if userlog != None:
                login(request, userlog)

                if request.user.is_superuser:
                    return redirect("panel")
                else:
                    return redirect("user_panel")

    return render(request, 'front/login.html')

def mylogout(request):
    logout(request)
    return redirect("mylogin")

def panel(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    return render(request, 'back/home.html')

def result(request, word):
    site=Main.objects.get(pk=1)
    now=datetime.datetime.now()
    year=now.year
    month=now.month
    day=now.day
    if len(str(day))==1:
        day="0"+str(day)
    if len(str(month))==1:
        month="0"+str(month)

    today=str(day)+"/"+str(month)+"/"+ str(year)
    if request.method=="POST":
        print(word)
        question=Question.objects.filter(subject=word)
        name=request.POST.get("name")
        email=request.POST.get("email")
        correct=0
        ques=0
        for i in question:
            if i.answer==request.POST.get("answer"+str(i.pk)):
                correct=correct+1
            ques=ques+1
        if ques <10:
            data=Record(name=name, email=email, subject=word, correctAnswer=correct, totalQuestion=ques, date=today)
            data.save()
        else:
            ques=10
            data=Record(name=name, email=email, subject=word, correctAnswer=correct, totalQuestion=ques, date=today)
            data.save()
        return render(request, 'front/result.html', {"correct":correct, "ques":ques, "name":name, "email":email, "site": site})
    else:
        return redirect("home")

def quiz(request, word):
    site=Main.objects.get(pk=1)
    li=[]
    question=Question.objects.filter(subject=word)
    sub=Subject.objects.all()
    for i in question:
        li.append(i)
    shuffle(li)

    if len(li) < 10:
        enumerated_li=enumerate(li, 1)
        return render(request, "front/quiz.html", {"sub": sub, "word":word, "question":enumerated_li, "site":site})
    else:
        enumerated_li=enumerate(li[:10], 1)
        return render(request, "front/quiz.html", {"question": enumerated_li,"sub": sub, "word":word, "site": site})

def site_setting(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end

    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        youtube=request.POST.get("youtube")
        twitter=request.POST.get("twitter")
        phone=request.POST.get("phone")
        about=request.POST.get("about")
        # Update the Main
        data=Main.objects.get(pk=1)
        data.name=name
        data.email=email
        data.youtube=youtube
        data.twitter=twitter
        data.phone=phone
        data.about=about
        data.save()

    site=Main.objects.get(pk=1)
    return render(request, 'back/setting.html', {"site": site})

def about_setting(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    if request.method == "POST":
        aboutAdmin = request.POST.get("aboutAdmin")

        if aboutAdmin == "":
            error = "About Field is required!!"
            return render(request, "back/error.html", {"error": error})
        data = Main.objects.get(pk=1)
        data.aboutAdmin = aboutAdmin
        data.save()

    about = Main.objects.get(pk=1).aboutAdmin

    return render(request, "back/about_setting.html", {"about": about})

def change_password(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    if request.method == "POST":
        oldpass = request.POST.get("oldpass")
        newpass = request.POST.get("newpass")
        if oldpass == "" or newpass == "":
            error = "Both fields are required!!"
            return render(request, "back/error.html", {"error": error})
        user = authenticate(username = request.user, password = oldpass)
        if user != None:
            if len(newpass) < 8:
                error = "Your password must be at least 8 character!!"
                return render(request, "back/error.html", {"error": error})
            count1 = 0
            count2 = 0
            count3 = 0
            # count4 = 0
            for i in newpass:
                if i > "0" and i < "9":
                    count1 = 1
                if i > "A" and i < "Z":
                    count2 = 1
                if i > "a" and i < "z":
                    count3 = 1
                # if i > "!" and i < "(":
                #     count4 = 1
            if count1 == 1 and count2 == 1 and count3 == 1:
                data = User.objects.get(username = request.user)
                data.set_password(newpass)
                data.save()
                return redirect("mylogout")
        else:
            error = "Incorrect Password"
            return render(request, "back/error.html", {"error": error})

    return render(request, "back/change_password.html")

def myregister(request):
    if request.method == "POST":
        name = request.POST.get("name")
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        print(name, uname, email, password, repassword)
        if password != repassword:
            error = "Your password doesnot be matched"
            return render(request, "front/register.html", {"error": error})
        # Password Validation
        count1 = 0
        count2 = 0
        count3 = 0
        for i in password:
            if i > "0" and i < "9":
                count1 = 1
            if i > "A" and i < "Z":
                count2 = 1
            if i > "a" and i < "z":
                count3 = 1
            # if i > "!" and i < "(":
            #     count4 = 1
        if count1 == 0 or count2 == 0 or count3 == 0 :
            error = "Your password is not strong"
            return render(request, "front/register.html", {"error": error})
        if len(password) < 7:
            error = "Your password must be 7 character"
            return render(request, "front/register.html", {"error": error})
        if len(User.objects.filter(username = uname)) == 0 and len(User.objects.filter(email = email)) == 0:
            user = User.objects.create_user(username = uname, email = email, password = password)
            data = Manager(name= name, email= email, uname = uname)
            data.save()
            return redirect("mylogin")
    return render(request, "front/register.html")

def user_panel(request):
    # Login check start
    if not request.user.is_authenticated:
        return redirect("mylogin")
    # Login check end
    return render(request, "front/user/home.html")
