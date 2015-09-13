from django.db import models

class User(models.Model):
    #username = models.CharField(max_length=24, unique=True)
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
    password = models.CharField(max_length=18)
    address = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=10)
	payment_type = models.IntegerField(blank=True)
	payment_string = models.CharField(max_length = 100, blank=True)
	#transaction history???
	gender = models.BooleanField(default=False)
	license_number=models.CharField(max_length=20,blank=True)
	age = models.IntegerField(blank=True)
	university = models.CharField(max_length = 100, blank=True)
	#ratings???
	vehicle = models.ForeignKey(Vehicle)
	
class Vehicle(models.Model)
	max_seats = models.IntegerField(blank=True)
	