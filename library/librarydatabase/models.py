from django.db import models
from datetime import datetime,date

class signtable(models.Model):
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    memberid = models.CharField(max_length=200,primary_key=True)
    phone = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
       return self.name+"-"+self.memberid

class newbook(models.Model):
    bookname = models.CharField(max_length=200,default="null")
    bookid = models.CharField(max_length=200,primary_key=True, default="null")
    edition = models.CharField(max_length=200, default="null")
    price = models.CharField(max_length=200, default="null")
    page = models.IntegerField(default=0)
    author = models.CharField(max_length=200, default="null")
    genre = models.CharField(max_length=200, default="null")

    def __str__(self):
        return self.bookname+"-"+self.bookid

class issuebook(models.Model):
    memberid = models.ForeignKey(signtable,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default="null")
    department = models.CharField(max_length=200,default="null")
    bookid = models.ForeignKey(newbook,on_delete=models.CASCADE)
    bookname = models.CharField(max_length=200,default="null")
    author = models.CharField(max_length=200,default="null")
    issuedate = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    def __str__(self):
        return self.bookname+"-"+self.name

class returnbook(models.Model):
    memberid = models.ForeignKey(signtable,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default="null")
    department = models.CharField(max_length=200,default="null")
    bookid = models.ForeignKey(newbook,on_delete=models.CASCADE)
    bookname = models.CharField(max_length=200,default="null")
    author = models.CharField(max_length=200,default="null")
    returndate = models.DateField(auto_now_add=False,auto_now=False,blank=True)

    def __str__(self):
        return self.bookname+"-"+self.name

class testing(models.Model):
    myname = models.CharField(max_length=200,default="null")
    password = models.CharField(max_length=200,default="null")
    def __str__(self):
        return self.myname+"-"+self.password