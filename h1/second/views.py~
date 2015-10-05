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
    r2 = requests.get('http://models-api:8000/models/get_user/' + str(driver_pk))
    ok = json.loads(r2.text)['ok']
    if(ok != True):
        driver = "Driver Not Found"
    else:
        driver_model = json.loads(r2.text)['user']
        driver_details = json.loads(driver_model[1:-1])['fields']
        driver = driver_details['first'] + " " + driver_details['last']
    r3 = requests.get('http://models-api:8000/models/get_car/' + str(vehicle_pk))
    ok = json.loads(r3.text)['ok']
    if(ok != True):
        vMake = "Not Found"
        vModel = "Not Found"
    else:
        car_model = json.loads(r3.text)['car']
        car_details = json.loads(car_model[1:-1])['fields']
        vMake = car_details['make']
        vModel = car_details['model']
    return JsonResponse({'ok':True, 'driver': driver, 'vMake': vMake, 'vModel': vModel, 'leave': details['leave_time'], 'start': details['start'], 'arrive': details['arrive_time'], 'Destination': details['destination']})
