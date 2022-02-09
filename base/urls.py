from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us/', views.aboutUs, name="about-us"),
    path('our-product/', views.ourProduct, name="our-product"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('scheduler/', views.scheduler, name="scheduler"),
    path('status/', views.status, name="status"),
    path('reset-password/', views.resetPassword, name="reset-password"),
    path('add-pet/', views.addPet, name="add-pet")
]
