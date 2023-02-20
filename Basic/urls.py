from django.contrib import admin
from django.urls import path
from Basic import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('know', views.know, name='know'),
    path('contact', views.contact, name='contact'),
    path('post/', views.GetDetail, name='Get Detail'),
    path('find_item', views.find_item, name='find_item')
]