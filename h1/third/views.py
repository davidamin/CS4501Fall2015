from django.shortcuts import render,render_to_response, get_object_or_404
from django.template import Context, RequestContext, loader
from django.template.loader import get_template
from django.http import HttpResponse
from django.http import JsonResponse
from django import forms
from .forms import LoginForm
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
	if request.method == 'GET':
		login_form = LoginForm()
		return render_to_response("login.html", 
			{'login_form':login_form},
			context_instance=RequestContext(request))
	else:
		login_form = LoginForm(request.POST)
		if not login_form.is_valid():
			return render_to_response("login.html", 
			{'login_form':login_form, 'input': False},
			context_instance=RequestContext(request))
		username = login_form.cleaned_data['username']
		password = login_form.cleaned_data['password']
		resp = requests.post('http://exp-api:8000/exp/login/', data=request.POST)
		ok = json.loads(resp.text)['ok']
		if not ok:
			return render_to_response("login.html",
			{'login_form':login_form, 'valid': False},
			context_instance=RequestContext(request))
		authenticator = json.loads(resp.text)['auth']['auth']
		response = HttpResponseRedirect('/')
		response.set_cooke("auth", authenticator)
		return response
			
