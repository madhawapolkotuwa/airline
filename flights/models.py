from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    #origin = models.CharField(max_length=64)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") 
    #models.CASCADE:- if two tables are cascade when delete the one item efect to also the other table also
    #related_name="" give the resonable name
    
    #destination = models.CharField(max_length=64,)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals") 
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin}: {self.destination}: {self.duration}"
    
    def is_valid_flight(self):
        return self.origin != self.destination or self.duration > 0
    

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
