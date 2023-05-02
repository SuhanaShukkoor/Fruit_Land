from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"index.html")

def test1(request):
    return render(request,"test.html",{"val":"java"})

def login(request):
    if request.method=="POST":
        uname=request.POST["user"]
        pname=request.POST["pas"]
        u=auth.authenticate(username=uname,password=pname)
        if u:
            auth.login(request,u)
            return redirect("/")
        msg="Invalid username and password"
        return render(request,"login.html",{"msg":msg})
    else:
        return render(request,"login.html")

def register(request):
    if request.method=="POST":
        Fname=request.POST["fname"]
        Lname=request.POST["lname"]
        Uname=request.POST["user"]
        Email=request.POST["email"]
        pname=request.POST["pas"]
        repas=request.POST["repas"]
        if pname==repas:
            if User.objects.filter(username=Uname):
                msg="username is already taken"
                return render(request,"register.html",{"msg":msg})
            elif User.objects.filter(email=Email):
                msg="Email is already taken"
                return render(request,"register.html",{"msg":msg})
            else:
                user=User.objects.create_user(first_name=Fname,last_name=Lname,username=Uname,email=Email,password=pname)
                user.save();
                auth.login(request,user)
                return redirect("/")

                
        else:
            msg="Password invalid"
            return render(request,"register.html",{"msg":msg})
    
    else:
        return render(request,"register.html")
    
def logout(request):
    auth.logout(request)
    return redirect("/")


