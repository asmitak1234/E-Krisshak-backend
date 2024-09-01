# <!-- Made By - Asmita Kumari -->

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Krisshak(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="krisshaks")
    krisshakId=models.AutoField(primary_key=True)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Address=models.CharField(max_length=500)
    Email=models.CharField(max_length=100)
    RegistrationNo=models.CharField(max_length=100)
    Age=models.FloatField()
    Experience=models.FloatField()
    MasteryGrow=models.CharField(max_length=200)
    HighestEducation=models.CharField(max_length=100)
    

    def __str__(self):
        return self.Email