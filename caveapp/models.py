from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    """Booking table"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date_check_in = models.DateTimeField()
    date_check_out = models.DateTimeField()
    number = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.user.username})"

    








# create contantacts models here
class Contacts (models.Model):
    """Our contacts"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject= models.TextField()
    message = models.TextField()




    #To return the values in human readable formats

    def __str__(self):
        return self.name
    
    