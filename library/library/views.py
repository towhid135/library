from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")
def usersignup(request):
    return render(request,"signup.html")
def forgotpass(request):
    return render(request,"forgot.html")
def addnewbook(request):
    return render(request, "addbook.html")
def foradmin(request):
    return render(request, "foradmin.html")
def forstudent(request):
    return render(request, "forstudent.html")
