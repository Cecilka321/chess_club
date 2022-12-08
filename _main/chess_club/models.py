from django.db import models


class Members(models.Model):
    objects = []
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    birthyear = models.IntegerField()
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    rating = models.IntegerField()

# Create your models here.


