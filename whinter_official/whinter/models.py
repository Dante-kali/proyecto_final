from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

# class Booking:
    
#     def __init__(self, name, service):
#         self.name = name
#         self.service = service
        
#     def __str__(self):
#         return f'this is a booking for {self.name} and request {self.service}'

class Booking(models.Model):
    
    name = models.CharField(max_length=50)
    service = models.CharField(max_length=50)

    def __str__(self):
        return f'this is a booking for {self.name} and request {self.service}'