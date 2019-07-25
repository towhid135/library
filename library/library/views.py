from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from librarydatabase import models

def returnbook(request):
    return render(request,"return.html")
def issuebook(request):
    return render(request,"issue.html")


def search(request):
    if (request.method=="POST"):
        findbookname = request.POST.get("findbookname")
        bookcheak = models.newbook.objects.filter(bookname=findbookname)
        sample_instance = models.newbook.objects.get(bookid=1)
        value_of_name = sample_instance.bookname
        print(value_of_name)
        if bookcheak:
            findobj = models.newbook.objects.filter(bookname=findbookname)
            context = {"find":findobj}
            return render(request,"search.html",context)
        else:
            return render(request,"search.html")
    else:
        return render(request, "search.html")


def exam(request):
    inp = "12345678"
    demo = models.testing.objects.filter(password=inp)
    context = {"tes":demo}
    return render(request,"example.html",context)

def home(request):
    if (request.method=="POST"):
        h_role = request.POST.get("h_role")
        h_user = request.POST.get("h_user")
        h_pass = request.POST.get("h_pass")
        cheak = models.signtable.objects.filter(role=h_role, user=h_user, password=h_pass)
        print(h_role+" "+h_user+" "+h_pass);
        if cheak:
            if h_role == "Librarian" :
                return render(request,"foradmin.html")
            elif h_role=="Member":
               return render(request, "forstudent.html")
            else:
                return render(request,"home.html")
        else:
            return render(request,"home.html")

    else:
        return render(request,"home.html")

def usersignup(request):
    if (request.method=='POST'):
        s_user = request.POST.get("s_user")
        s_pass = request.POST.get("s_pass")
        s_name = request.POST.get("s_name")
        s_depart = request.POST.get("s_depart")
        s_id = request.POST.get("s_id")
        s_phone = request.POST.get("s_phone")
        s_role = request.POST.get("s_role")
        obj2 = models.signtable(user = s_user,password = s_pass,name = s_name,department = s_depart,memberid = s_id,phone = s_phone,role = s_role)
        obj2.save()
        if obj2:
            return render(request,"home.html")
        else:
            return render(request,"signup.html")
    else:
        return render(request, "signup.html")

def forgotpass(request):
    if (request.method=="POST"):
        f_user = request.POST.get("f_user")
        f_phone = request.POST.get("f_phone")
        f_cheak = models.signtable.objects.filter(user=f_user,phone=f_phone)
        if f_cheak:
            obj_sign = models.signtable.objects.filter(phone=f_phone)
            context = {"getpass":obj_sign}
            return render(request,"forgot.html",context)
        else:
            return render(request,"forgot.html")
    else:
        return render(request, "forgot.html")



def addnewbook(request):
    if (request.method=='POST'):
        name1 = request.POST.get("name1")
        id1 = request.POST.get("id1")
        edition1 = request.POST.get("edition1")
        price1 = request.POST.get("price1")
        page1 = request.POST.get("page1")
        author1 = request.POST.get("author1")
        genre1 = request.POST.get("genre1")
        obj1 = models.newbook(bookname = name1,bookid = id1,edition = edition1,price = price1,page = page1,author = author1,genre = genre1)
        obj1.save()
        return render(request,"addbook.html")
    else:
        return render(request, "addbook.html")

def foradmin(request):
    return render(request, "foradmin.html")
def forstudent(request):
    return render(request, "forstudent.html")
def showbook(request):
    bookinfo = models.newbook.objects.all()
    context = {"book":bookinfo}
    return render(request,'available.html',context)
