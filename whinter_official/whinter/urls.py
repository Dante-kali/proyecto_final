from django.contrib import admin
from django.urls import path

from .views import home, search, list, create

urlpatterns = [   
    path("", home), 
    path('list/', list),
    path("searching/<name>", search),
    path('create/<name>/<service>', create),
]