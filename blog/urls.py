from django.urls import path  
from . import views

#urls is a submodule within Django that deals with URL routing and mapping URLs to views.

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='abou-home')
   
]
