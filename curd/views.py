from django.shortcuts import render,redirect
from curd.models import All_Employee
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def CreateDetails(request):
    return render(request,"index.html")


def SaveDetails(request):
    a =request.POST.get("t1")
    b=request.POST.get("t2")
    c=request.POST.get("t3")
    d=request.POST.get("t4")
    e=request.POST.get("t5")
    f=request.POST.get("t6")
    # g=request.POST.get("t7")
    # h=request.POST.get("t8")
    All_Employee(idno=a,name=b,age=c,contact_no=d,gender=e,deginations=f).save()
    messages.success(request,"Registrations success")
    return redirect("main")


def Showall(request):
    sss =All_Employee.objects.all()
    pa =Paginator(sss,1)
    page_no =request.GET.get("page_no",1)
    data=pa.page(page_no)
    return render(request,"show.html",{"data":data})


def update(request):
    no = request.GET.get("u1")
    res =All_Employee.objects.get(idno=no)
    return render(request,"update.html",{"data":res})


def all_update(request):
    i = request.POST.get("u1")
    nm =request.POST.get("u2")
    ag = request.POST.get("u3")
    cn =request.POST.get("u4")
    gn =request.POST.get("u5")
    dg = request.POST.get("u6")
    All_Employee.objects.filter(idno=i).update(name=nm,age=ag,contact_no=cn,gender=gn,deginations=dg)
    return redirect("view")


def delete(request):
    re =request.GET.get("no")
    All_Employee.objects.filter(idno=re).delete()

    return redirect("view")