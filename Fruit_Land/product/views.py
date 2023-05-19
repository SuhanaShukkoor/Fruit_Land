from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import fruits,commentbox
from django.http import JsonResponse
from django.core.cache import cache


# Create your views here.

def about(request):
    iname=request.GET['id']
    obj=fruits.objects.get(id=iname)
    if "recent" in request.session:
        if iname in request.session["recent"]:
            request.session["recent"].remove(iname)
        rect=fruits.objects.filter(id__in=request.session["recent"])
        request.session["recent"].insert(0,iname)
        if len(request.session["recent"])>4:
            request.session["recent"].pop()
    else:
        rect=[]
        request.session["recent"]=[iname]
    request.session.modified=True
        

    return render(request,"about.html",{"data":obj,"rct":rect})

def comment(request):
    com=request.GET['cmtmsg']
    com1=request.GET['proid']
    com2=request.GET['user']
    obj=commentbox.objects.create(user=com2,msg=com,proid_id=com1,like=0)
    obj.save()
    return redirect("/product/?id="+com1)

def like(request):
    lik=request.GET['id']
    obj=commentbox.objects.filter(id=lik)
    l=int(obj[0].like)+1
    obj.update(like=str(l))
    return redirect("/product/?id="+str(obj[0].proid_id))

def autoc(request):
    if "term" in request.GET:
        data=request.GET["term"]
        obj=fruits.objects.filter(name__istartswith=data)
        a=[]
        for i in obj:
            a.append(i.name)
            print(a)
        print("hello",obj) 
        return JsonResponse(a,safe=False)
    return render(request,"test.html")

def about2(request):
    iname=request.GET['id']
    if cache.get(iname):
        print("DATA FROM CACHE")
        obj=cache.get(iname)
    else:
        obj=fruits.objects.get(id=iname)
        cache.set(iname,obj)
        print("DATA FROM DATABASE")
    return render(request,"about.html",{"data":obj})

