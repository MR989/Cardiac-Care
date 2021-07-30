
from django.contrib import admin
from django.urls import path
from CardiaCare import views
urlpatterns = [
    path("home",views.home,name='home'),
    path("result",views.result,name='result'),
    path("",views.index,name='index'),
]









