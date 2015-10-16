from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import requests

# Create your views here.

def ride_detail(request, ride):
    r = requests.get('http://models-api:8000/models/get_ride/' + ride)
    ok = json.loads(r.text)['ok']
    if(ok != True):
        return JsonResponse({'ok':False})
    ride = json.loads(r.text)['car']
    details = json.loads(ride[1:-1])['fields']
    driver_pk = details['driver']
    vehicle_pk = details['car']
    return JsonResponse({'ok':True, 'driver': 'David Amin', 'vMake': 'Chevy', 'vModel': 'Trailblazer', 'leave': details['leave_time'], 'start': details['start'], 'arrive': details['arrive_time'], 'Destination': details['destination']})

def home_detail(request):
    r = requests.get('http://models-api:8000/models/ride_list')
    ok = json.loads(r.text)['ok']
    if(ok != True):
        return JsonResponse({'ok':False})
    ride = json.loads(r.text)['car']
    details = json.loads(ride[1:-1])['fields']
    driver_pk = details['driver']
    vehicle_pk = details['car']
    return JsonResponse({'ok':True, 'driver': 'David Amin', 'vMake': 'Chevy', 'vModel': 'Trailblazer', 'leave': details['leave_time'], 'start': details['start'], 'arrive': details['arrive_time'], 'Destination': details['destination']})

    