from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label = 'User Name', max_length=24)
	password = forms.CharField(widget = forms.PasswordInput())

class CreateVehicle(forms.Form):
	make = forms.CharField(label = "Make", max_length=30)
	model = forms.CharField(label = "Model", max_length=30)
	year = forms.IntegerField(label = "Year")
	color = forms.CharField(label = "Color", max_length=15)
	plates = forms.CharField(max_length= 10, label = "License Plate")
	max_seats = forms.IntegerField(label = "Maximum # of Seats")
	trunk_space = forms.FloatField(label = "Available Trunk Space")
	condition = forms.CharField(max_length = 100, label = "Condition")
	accomodations = forms.CharField(max_length=30, label = "Special Accomodations")
	road_assistance = forms.CharField(max_length=30, label = "Roadside-Assistance Coverage")
	uninsured = forms.BooleanField(label = "Insured Driver", required=False)
	notes = forms.CharField(max_length = 500, label = "Notes")