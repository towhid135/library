from django.shortcuts import render
from django.http import HttpResponse
from librarydatabase import models
from django.db.models import Subquery
#from django.contrib.auth.models import *

def returnbook(request):
    if (request.method=='POST'):
        r_mid = request.POST.get("r_mid")
        r_bid = request.POST.get("r_bid")
        return_date = request.POST.get("r_date")
        if r_mid and r_bid and return_date:
            getissue = models.issuebook.objects.get(memberid=r_mid, bookid=r_bid)
            if getissue:
                print("first if")
                getmem = models.signtable.objects.get(memberid=r_mid)
                getbook = models.issuebook.objects.get(bookid=r_bid)
                if getmem and getbook:
                    print("second if")
                    objreturn = models.returnbook(memberid=getmem, name=getmem.name, department=getmem.department,bookid=getbook.bookid, bookname=getbook.bookname, author=getbook.author,edition=getbook.edition,price=getbook.price,page=getbook.page,genre=getbook.genre,returndate=return_date)
                    objreturn.save()
                    obj_add_book = models.newbook(bookname = getbook.bookname,bookid = r_bid,edition = getbook.edition,price = getbook.price,page = getbook.page,author = getbook.author,genre = getbook.genre)
                    obj_add_book.save()
                    getissue.delete()
                    return render(request, "return.html")
                else:
                    print("first else")
                    return render(request, "return.html")
            else:
                print("second else")
                return render(request, "return.html")
        else:
            return render(request, "return.html")

    else:
        print("third else")
        return render(request,"return.html")



def issuebook(request):
    if (request.method=='POST'):
        i_mid = request.POST.get("i_mid")
        i_bid = request.POST.get("i_bid")
        issue_date = request.POST.get("i_date")
        if i_mid and i_bid and issue_date:
            getmem = models.signtable.objects.get(memberid=i_mid)
            getbook = models.newbook.objects.get(bookid=i_bid)
            if getmem and getbook:
                objissue = models.issuebook(memberid=getmem, name=getmem.name, department=getmem.department, bookid=getbook.bookid, bookname=getbook.bookname, author=getbook.author,edition = getbook.edition,price = getbook.price,page = getbook.page,genre = getbook.genre,issuedate=issue_date)
                #print("true")
                objissue.save()
                getbook.delete()


                return render(request, "issue.html")
            else:
                return render(request, "issue.html")
        else:
            return render(request, "issue.html")
    else:
        return render(request,"issue.html")


def search(request):
    if (request.method=="POST"):
        findbookname = request.POST.get("findbookname")
        #bookcheak = models.newbook.objects.filter(bookname__iexact=findbookname)
        bookcheak = models.newbook.objects.filter(bookname__contains = findbookname).order_by('bookname')
        if bookcheak and findbookname:
            context = {"find":bookcheak}
            return render(request,"search.html",context)
        else:
            st = ''
            for j in findbookname:
                if j != ' ':
                    st += j
                else:
                    break;
            if findbookname:
                bookcheak = models.newbook.objects.filter(bookname__startswith = st).order_by('bookname')
                if bookcheak:
                    context = {"find": bookcheak}
                    return render(request, "search.html", context)
                else:
                    st = st[0]
                    bookcheak = models.newbook.objects.filter(bookname__startswith=st).order_by('bookname')
                    context = {"find": bookcheak}
                    return render(request, "search.html", context)
            else:
                return render(request, "search.html")

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
        if h_role and h_user and h_pass:
            cheak = models.signtable.objects.filter(role=h_role, user=h_user, password=h_pass)
            if cheak:
                if h_role == "Librarian":
                    return render(request, "foradmin.html")
                elif h_role == "Member":
                    print("yes")
                    return render(request, "forstudent.html")
                else:
                    return render(request, "home.html")
            else:
                return render(request, "home.html")
        else:
            return render(request, "home.html")

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
        if s_user and s_pass and s_name and s_depart and s_id and s_phone and s_role:
            obj2 = models.signtable(user=s_user, password=s_pass, name=s_name, department=s_depart, memberid=s_id,phone=s_phone, role=s_role)
            obj2.save()
            print("returning home")
            return render(request, "home.html")
        else:
            return home(request)
    else:
        print("returning signup")
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
    bookinfo = models.newbook.objects.all().order_by('bookid')
    #separate = models.issuebook.objects.all();
    #bookinfo = models.newbook.objects.filter(bookid__in = Subquery(separate.values('bookid')))
    context = {"book":bookinfo}
    return render(request,'available.html',context)

def statisics(request):
    objiss = models.issuebook.objects.all().order_by('bookid')
    objret = models.returnbook.objects.all().order_by('bookid')
    context = {"iss":objiss,"ret":objret}
    return render(request,"statistics.html",context)
def availableforadmin(request):
    bookinfo = models.newbook.objects.all().order_by('bookid') #'-bookid' dile descending order
    context = {"book": bookinfo}
    return render(request,"availableforadmin.html",context)
def member(request):
    mem = models.signtable.objects.all().order_by('memberid')
    context = {'member':mem}
    return render(request,'member.html',context)
