from django.urls import path
from . import views


urlpatterns = [

path('' , views.main) , 
path('base/home.html' , views.home) ,
path('base/blog.html', views.blog) ,
path('base/Q1.html' , views.Q1 ) ,
path('base/Q2.html' , views.Q2 ) ,
path('base/Q3.html' , views.Q3 ) ,
path('base/Q4.html' , views.Q4 ) ,


]