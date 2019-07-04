from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('sign/',views.usersignup),
    path('forgot/',views.forgotpass),
    path('addnewbook/',views.addnewbook),
    path('adminview/',views.foradmin),
    path('studentview/', views.forstudent),
    path('admin/', admin.site.urls),
]

