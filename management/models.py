from django.db import models
from django.contrib.auth.models import User
class student(models.Model):
    fk = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    email = models.EmailField(max_length=254)
    contact = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()

class history(models.Model):
    contact = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
    dob = models.DateField()
    