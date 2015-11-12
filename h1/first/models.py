from django.db import models

class Vehicle(models.Model):
    max_seats = models.IntegerField(default=0,  null=True)
    trunk_space = models.FloatField(default= 0.0)
    notes = models.CharField(max_length = 500, blank=True)
    condition = models.CharField(max_length = 100, blank=True)
    make = models.CharField(max_length = 30, blank=True)
    model = models.CharField(max_length = 30, blank=True)
    year = models.IntegerField(default=0)
    color = models.CharField(max_length = 15, blank=True)
    plates = models.CharField(max_length = 10, blank=True)
    uninsured = models.BooleanField(default=False)
    road_assistance = models.CharField(max_length = 30, blank=True)
    accomodations = models.CharField(max_length = 30, blank=True)

class User(models.Model):
    username = models.CharField(max_length=24, unique=True)
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=256)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    phone_number = models.CharField(max_length=10)
    payment_type = models.IntegerField(blank=True)
    #payment_string = models.CharField(max_length = 100, blank=True)
    #transaction history???
    gender = models.BooleanField(default=False)
    license_number=models.CharField(max_length=20,blank=True)
    age = models.IntegerField(blank=True)
    #university = models.CharField(max_length = 100, blank=True)
    #ratings???
    vehicle = models.ForeignKey(Vehicle, blank=True, null=True)
    active = models.BooleanField(default=True)

class Ride(models.Model):
    car = models.ForeignKey(Vehicle)
    driver = models.ForeignKey(User)
    leave_time = models.DateTimeField(blank = True)
    arrive_time = models.DateTimeField(blank = True)
    destination = models.CharField(max_length = 30, blank = True)
    start = models.CharField(max_length = 30, blank = True)
    #riders
    #cost structure
    #planned stops
    comments = models.CharField(max_length = 300, blank = True)
    max_miles_offroute = models.FloatField(blank = True)
    active = models.BooleanField(default = True)

class AuthTable(models.Model):
    authenticator = models.CharField(max_length = 255, primary_key=True)
    user_id = models.ForeignKey(User)
    date_created = models.DateTimeField()
