from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

# Create your models here.

# class Booking:
    
#     def __init__(self, name, service):
#         self.name = name
#         self.service = service
        
#     def __str__(self):
#         return f'this is a booking for {self.name} and request {self.service}'

class Booking(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now) 
    hora_inicio = models.DateTimeField(default=timezone.now)
    hora_fin = models.DateTimeField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'this is a booking for {self.name} and request {self.service}'
