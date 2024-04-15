from django.contrib import admin
from django.urls import path

from .views import home, search, list, create, detail

urlpatterns = [   
    path("", home), 
    path('list/', list),
    path('detail/<booking_id>', detail),
    path("searching/<name>", search),
    path('create/<name>/<service>', create),
]