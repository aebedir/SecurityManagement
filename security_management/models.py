from django.db import models
from django.db import models

class SecurityGuard(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    years_of_experience = models.IntegerField()

    def __str__(self):
        return self.name

class DutyTime(models.Model):
    guard = models.ForeignKey(SecurityGuard, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.guard.name} - {self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')}"
