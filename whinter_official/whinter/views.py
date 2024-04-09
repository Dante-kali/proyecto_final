from django.shortcuts import render
from django.http import HttpResponse

from .models import Booking
# Create your views here.

# home
def home(request):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    date = {
        'date' : "Welcome to the Aplication 'Whinter'"
    }
    return render(request, 'template1.html', date)


# search name
def search(request, name):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    
    booking = Booking.objects.filter(name=name).all()
    context = {
        'name' : name,
        'bookings' : booking
    }
    return render(request, 'template2.html', context)

 
# client list
def list(request):
    print("-" * 100) 
    print("-" * 100)
    print(request.method)
    
    booking = Booking.objects.all()
    client_list= {
        'booking' : booking
    }
    return render(request, 'template3.html', client_list)


# create booking 
def create(request, name, service):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    booking = Booking.objects.create(name=name, service=service)
    return HttpResponse(f'the booking {booking}')