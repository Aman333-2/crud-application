import email
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=78)
    email=models.CharField(max_length=58)
    password=models.CharField(max_length=65)

