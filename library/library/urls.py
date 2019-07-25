from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('example/',views.exam),
    path('sign/',views.usersignup),
    path('forgot/',views.forgotpass),
    path('addnewbook/',views.addnewbook),
    path('adminview/',views.foradmin),
    path('studentview/', views.forstudent),
    path('return/', views.returnbook),
    path('issue/', views.issuebook),
    path('available/',views.showbook),
    path('search/',views.search),
    path('admin/', admin.site.urls),
]

