from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import requests

# Create your views here.

def ride_detail(request, ride):
    if request.method != 'GET':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be GET'})
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

def home_detail(request):
    if request.method != 'GET':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be GET'})
    r = requests.get('http://models-api:8000/models/ride_list')
    ok = json.loads(r.text)['ok']
    if(ok != True):
        return JsonResponse({'ok':False})
    ride = json.loads(r.text)['car']
    details = json.loads(ride[1:-1])['fields']
    driver_pk = details['driver']
    vehicle_pk = details['car']
    return JsonResponse({'ok':True, 'driver': 'David Amin', 'vMake': 'Chevy', 'vModel': 'Trailblazer', 'leave': details['leave_time'], 'start': details['start'], 'arrive': details['arrive_time'], 'Destination': details['destination']})

def create_user(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be POST'})
    r = requests.post('http://models-api:8000/models/add_user', data=request.POST)
    ok = json.loads(r.text)['ok']
    if ok:
        userpass = {}
        userpass['username'] = request.POST['username']
        userpass['password'] = request.POST['password']
        r2 = requests.post('http://models-api:8000/models/get_auth', data=userpass)
        d2 = json.loads(r2.text)['ok']
        if d2:
            auth = json.loads(r2.text)['auth']
        else:
            return JsonResponse({'ok': False, 'error': 'Encountered error while authenticating'})
    else:
        return JsonResponse({'ok': False, 'error': 'Encountered error while creating user'})
    return JsonResponse({'ok': True, 'auth': auth, 'log': 'User Created'})

def login(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be POST'})
    r = requests.post('http://models-api:8000/models/get_auth', data=request.POST)
    ok = json.loads(r.text)['ok']
    if ok:
        return JsonResponse({'ok': True, 'auth': json.loads(r.text)['auth']})
    else:
        return JsonResponse({'ok': False, 'error': 'Encountered error while authenticating'})

def logout(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be POST'})
    r = requests.post('http://models-api:8000/models/revoke_auth', data=request.POST)
    ok = json.loads(r.text)['ok']
    if ok:
        return JsonResponse({'ok': True, 'log': 'Authenticator revoked'})
    else:
        return JsonResponse({'ok': False, 'error': 'Encountered error while removing auth'})

def add_new_ride(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be POST'})
    auth = request.POST['auth']
    r = requests.post('http://models-api:8000/models/is_auth', data={'auth':auth})
    ok = json.loads(r.text)['ok']
    if ok:
        r2 = requests.post('http://models-api:8000/models/create_ride/', data=request.POST)
        d2 = json.loads(r2.text)['ok']
        if d2:
            return JsonResponse({'ok': True, 'log': 'Created Ride'})
        else:
            return JsonResponse({'ok': False, 'error': 'Failed to create ride'})
    else:
        return JsonResponse({'ok': False, 'error': 'Invalid authentication to make ride'})

def add_new_vehicle(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be POST'})
    auth = request.POST['auth']
    auth_req = requests.post('http://models-api:8000/models/is_auth', data={'auth':auth})
    ok = json.loads(auth_req.text)['ok']
    if ok:
        resp = requests.post('http://models-api:8000/models/add_vehicle', data=request.POST)
        created = json.loads(resp.text)['ok']
        if created:
            return JsonResponse({'ok': True, 'log': 'Added vehicle'})
        else:
            return JsonResponse({'ok': False, 'error': 'Failed to create vehicle'})
    else:
        return JsonResponse({'ok': False, 'error': 'Invalid authentication to make vehicle'})