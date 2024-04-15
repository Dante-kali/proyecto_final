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
    return render(request, 'index.html', date)


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
    return render(request, 'search.html', context)

 
# client list
def list(request):
    print("-" * 100) 
    print("-" * 100)
    print(request.method)
    
    booking = Booking.objects.all()
    client_list= {
        'bookings' : booking
    }
    return render(request, 'list.html', client_list)


# create booking 
def create(request, name, service):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    booking = Booking.objects.create(name=name, service=service)
    booking = {
        'booking' : booking
    }
    return render(request, 'create.html', booking)


def detail(request, booking_id):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    reserva = Booking.objects.get(id = booking_id)
    reserva = {
        'reserva' : reserva
    }
    return render(request, 'detail.html', reserva)