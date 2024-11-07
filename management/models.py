from django.db import models

class student(models.Model):
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
    