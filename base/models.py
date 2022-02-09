from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=False)

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    add_breed = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=8)
    age = models.IntegerField(null=False)
    dob = models.DateField()
    height = models.DecimalField(max_digits=1000, decimal_places=3)
    weight = models.DecimalField(max_digits=1000, decimal_places=3)
    activity = models.CharField(max_length=100)
    meal = models.CharField(max_length=100)
    dislike = models.CharField(max_length=100)
    allergies = models.CharField(max_length=100)
    prefer_food = models.CharField(max_length=100)
    help_required = models.CharField(max_length=100)