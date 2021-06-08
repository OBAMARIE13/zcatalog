from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('envoi/', views.envoi, name='envoi'),
    path('video/', views.video, name='video'),
    path('phodetail/', views.photodetail, name='photo-detail'),
]
