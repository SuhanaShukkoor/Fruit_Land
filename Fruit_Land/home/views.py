from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request,"index.html")

def test1(request):
    return render(request,"test.html",{"val":"java"})

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def loginsub(request):
    uname=request.GET["user"]
    pname=request.GET["pas"]
    u=auth.authenticate(username=uname,password=pname)
    if u:
        auth.login(request,u)
        return redirect("/")
    return render(request,"login.html",{"val":u})

def regsub(request):
    Fname=request.GET["fname"]
    Lname=request.GET["lname"]
    Uname=request.GET["user"]
    Email=request.GET["email"]
    pname=request.GET["pas"]
    repas=request.GET["repas"]
    

    return render(request,"test.html",{"val":Fname})

