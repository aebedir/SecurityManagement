from django.db import models
from django.db import models

from django.db import models

class Place(models.Model):
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.place

class DutyTime(models.Model):    
    time = models.CharField(max_length=100) 

    def __str__(self):
        return self.time

class SecurityGuard(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    years_of_experience = models.IntegerField()
    duty_times = models.ForeignKey(DutyTime, on_delete=models.CASCADE)  # ForeignKey ile DutyTime modeline referans veriliyor
    guard_place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"




