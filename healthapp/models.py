from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    message = models.CharField(max_length=250, blank=True, default='')

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.date}"