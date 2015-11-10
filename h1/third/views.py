from django.shortcuts import render,render_to_response, get_object_or_404
from django.template import Context, RequestContext, loader
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django import forms
from .forms import LoginForm, CreateVehicle, CreateUser
import json
import requests

# Create your views here.

def custom_processor(request):
    return {
        "first": "david",
        "last": "amin",
    }

def view_normal(request):
    return render_to_response("main.html", {"ID": "1",
	"Driver":"Elon Musk",
	"SPlace": "Charlottesville, VA",
	"EPlace": "Fairfax, VA",
	"DTime": "9:00am",
	"ETA": "11:00am",
	"DetourMiles": "20 Mi",
	"Seats": "3",
	"SeatCost": "$10",
	},
    context_instance=RequestContext(request, processors=[custom_processor]))

def ride_detail(request, ride):
    r = requests.get('http://exp-api:8000/exp/ride_detail/' + str(ride))
    return render_to_response("detail.html", {"Driver": json.loads(r.text)['driver'],
        "vMake": json.loads(r.text)['vMake'],
        "vModel": json.loads(r.text)['vModel'],
        "leave": json.loads(r.text)['leave'],
        "start": json.loads(r.text)['start'],
        "arrive": json.loads(r.text)['arrive'],
        "Destination": json.loads(r.text)['Destination'],
        },
    context_instance=RequestContext(request))

def login(request):
	auth = request.COOKIES.get('auth')
	if auth:
		return HttpResponseRedirect('/')
	if request.method == 'GET':
		login_form = LoginForm()
		return render_to_response("login.html", 
			{'login_form':login_form},
			context_instance=RequestContext(request))
	else:
		login_form = LoginForm(request.POST)
		if not login_form.is_valid():
			return render_to_response("login.html", 
			{'login_form':login_form, 'Response': "Invalid Input. Please try again."},
			context_instance=RequestContext(request))
		resp = requests.post('http://exp-api:8000/exp/login/', data=request.POST)
		ok = json.loads(resp.text)['ok']
		if not ok:
			return render_to_response("login.html",
			{'login_form':login_form, 'Response': "Incorrect Username/Password combination. Please try again."},
			context_instance=RequestContext(request))
		authenticator = json.loads(resp.text)['auth']
		response = HttpResponseRedirect('/')
		response.set_cookie("auth", authenticator)
		return response

def logout(request):
	auth = request.COOKIES.get('auth')
	if not auth:
		return HttpResponseRedirect('/v1/login/')
	resp = requests.post('http://exp-api:8000/exp/logout/', data={'auth':auth})
	ok = json.loads(resp.text)['ok']
	response = HttpResponseRedirect('/')
	response.delete_cookie('auth')
	return response

def create_user(request):
	auth = request.COOKIES.get('auth')
	if auth:
		return HttpResponseRedirect('/')
	if request.method == 'GET':
		creation_form = CreateUser()
		return render_to_response("create_user.html",
			{'creation_form': creation_form},
			context_instance=RequestContext(request))
	else:
		creation_form = CreateUser(request.POST)
		if not creation_form.is_valid():
			return render_to_response("create_user.html",
				{'creation_form': creation_form, 'Response': "Invalid Input. Please try again."},
				context_instance=RequestContext(request))
		resp = requests.post('http://exp-api:8000/exp/create_user/', data=request.POST)
		ok = json.loads(resp.text)['ok']
		if not ok:
			return render_to_response("create_user.html",
				{'creation_form': creation_form, 'Response': "There was an error while attempting to create the user"},
				context_instance=RequestContext(request))
		return render_to_response("create_user.html",
			{'creation_form': creation_form, 'Response': "User sucessfully created."},
			context_instance=RequestContext(request))

def create_vehicle(request):
	auth = request.COOKIES.get('auth')
	if not auth:
		return HttpResponseRedirect('/v1/login/')
	if request.method == 'GET':
		creation_form = CreateVehicle()
		return render_to_response("create_vehicle.html",
			{'creation_form': creation_form},
			context_instance=RequestContext(request))
	else:
		creation_form = CreateVehicle(request.POST)
		if not creation_form.is_valid():
			return render_to_response("create_vehicle.html",
				{'creation_form': creation_form, 'Response': "Invalid Input. Please try again."},
				context_instance=RequestContext(request))
		
		post_values = request.POST.copy()
		post_values['auth'] = auth

		resp = requests.post('http://exp-api:8000/exp/create_vehicle/', data=post_values)
		ok = json.loads(resp.text)['ok']
		if not ok:
			return render_to_response("create_vehicle.html",
				{'creation_form': creation_form, 'Response': "There was an error while attempting to add the vehicle."},
				context_instance=RequestContext(request))
		return render_to_response("create_vehicle.html",
			{'creation_form': creation_form, 'Response': "Vehicle succesfully added."})
