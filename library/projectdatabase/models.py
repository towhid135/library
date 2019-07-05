from django.db import models

class  signuptable(models.Model):
    user = models.CharField(max_length=200,default="null")
    password = models.CharField(max_length=200,default="null")
    name = models.CharField(max_length=200,default="null")
    department=models.CharField(max_length=200,default="null")
    ID = models.CharField(max_length=200,primary_key=True,default="null")
    sequrity = models.CharField(max_length=200,default="null")
    answer = models.CharField(max_length=200,default="null")
    role = models.CharField(max_length=15,default="null")

    def __str__(self):
        return self.name + "-" + self.ID
