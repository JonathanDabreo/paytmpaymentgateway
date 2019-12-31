from django.db import models
from django.urls import reverse

# Create your models here.

class data_of_user(models.Model):
    first=models.CharField(max_length=20)
    last=models.CharField(max_length=20)
    email=models.EmailField()
    semester=models.IntegerField(max_length=200)
    address=models.TextField(max_length=200)
    zipcode=models.IntegerField(max_length=200)
    amount=models.IntegerField(default="400")


    def __str__(self):
        return self.first
    
