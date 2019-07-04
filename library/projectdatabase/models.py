from django.db import models

class  logintable(models.Model):
    role = models.CharField(max_length=15)
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
