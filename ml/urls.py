from django.contrib import admin
from django.urls import path
from .views import index, result

urlpatterns = [
    path('',index),
    path('result',result)
]
