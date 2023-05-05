from django.shortcuts import render
from django.http import HttpResponse
from .models import fruits

# Create your views here.

def about(request):
    iname=request.GET['id']
    obj=fruits.objects.get(id=iname)
    return render(request,"about.html",{"data":obj})

def comment(request):
    return render(request,"test.html")

def like(request):
    return render(request,"test.html")