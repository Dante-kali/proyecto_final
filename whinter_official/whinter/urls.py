from django.contrib import admin
from django.urls import path

from .views import home, list, detail, create, search_form,  create_sala

urlpatterns = [   
    path("", home), 
    path('list/', list),
    path('detail/<booking_id>', detail),
    path('searching-form', search_form, name='search'),
    path('create/<name>/<service>', create),
    # path('create-form', create_form, name='create-form'),
    path('create-sala', create_sala, name='create_sala')
]