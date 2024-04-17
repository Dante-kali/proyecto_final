from django.contrib import admin
from django.urls import path

from .views import home, list, detail, create, search_form, create_form, create_sala

urlpatterns = [   
    path("", home), 
    path('list/', list),
    path('detail/<booking_id>', detail),
    path('searching-form', search_form, name='search'),
    path('create/<name>/<service>', create),
    path('create-sala', create_form, name='create'),
    path('create_form', create_sala, name='crear-sala-con-form')
]