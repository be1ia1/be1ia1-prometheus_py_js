from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ahula', views.ahula, name='ahula'),
    path('david', views.david, name='david')
]