from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
from django.utils.dateparse import parse_datetime
import json
import requests
from kafka import SimpleProducer, KafkaClient
from elasticsearch import Elasticsearch

# Create your views here.
kafka = KafkaClient('kafka:9092')
producer = SimpleProducer(kafka)
es = Elasticsearch(['es'])

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
        driver_details = json.loads(driver_model)['fields']
        driver = driver_details['first'] + " " + driver_details['last']
    r3 = requests.get('http://models-api:8000/models/get_car/' + str(vehicle_pk))
    ok = json.loads(r3.text)['ok']
    if(ok != True):
        vMake = "Not Found"
        vModel = "Not Found"
    else:
        car_model = json.loads(r3.text)['car']
        car_details = json.loads(car_model)['fields']
        vMake = car_details['make']
        vModel = car_details['model']
    return JsonResponse({'ok':True, 'driver': driver, 'vMake': vMake, 'vModel': vModel, 'leave': details['leave_time'], 'start': details['start'], 'arrive': details['arrive_time'], 'Destination': details['destination']})

def home_detail(request):
    if request.method != 'GET':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be GET'})
    r = requests.get('http://models-api:8000/models/all_rides')
    ok = json.loads(r.text)['ok']
    if(ok != True):
        return JsonResponse({'ok':False})
    ride = json.loads(r.text)['ride']
    result_set = []
    for r in ride:
        details = json.loads(r)['fields']
        driver_pk = details['driver']
        vehicle_pk = details['car']
        req_driver = requests.get('http://models-api:8000/models/get_user/' + str(driver_pk))
        req_vehicle = requests.get('http://models-api:8000/models/get_car/' + str(vehicle_pk))
        resp_driver = json.loads(json.loads(req_driver.text)['user'])['fields']            
        resp_vehicle = json.loads(json.loads(req_vehicle.text)['car'])['fields']
        leavetime = parse_datetime(details['leave_time'])
        arrivetime = parse_datetime(details['arrive_time'])
        ride_info = {'driver':resp_driver['first'], 'vMake': resp_vehicle['make'], 'vModel':resp_vehicle['model'], 'leave': leavetime.strftime("%B %d %-I:%M:%S %p"), 'start': details['start'], 'arrive': arrivetime.strftime("%B %d %-I:%M:%S %p"), 'Destination': details['destination']}
        result_set.append(ride_info)
    return JsonResponse({'ok':True, 'result_set': result_set})

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
        username = json.loads(r.text)['username']

        post_values = request.POST.copy()
        post_values['username'] = username

        r2 = requests.post('http://models-api:8000/models/add_ride', data=post_values)
        d2 = json.loads(r2.text)['ok']
        ride_id = json.loads(r2.text)['id']
        post_copy = request.POST.copy()
        post_copy['id'] = ride_id
        if d2:
            try:
                producer.send_messages(b'new-listings-topic', json.dumps(post_copy).encode('utf-8'))
            except Exception:
                #This is ugly, but if the topic doesn't exist we just try again. More than once is a problem though so we let that happen
                producer.send_messages(b'new-listings-topic', json.dumps(post_copy).encode('utf-8'))
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
        username = json.loads(auth_req.text)['username']

        post_values = request.POST.copy()
        post_values['username'] = username
        resp = requests.post('http://models-api:8000/models/add_vehicle', data=post_values)
        created = json.loads(resp.text)['ok']
        if created:
            return JsonResponse({'ok': True, 'log': 'Added vehicle'})
        else:
            return JsonResponse({'ok': False, 'error': 'Failed to create vehicle'})
    else:
        return JsonResponse({'ok': False, 'error': 'Invalid authentication to make vehicle'})

def search_result(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be POST'})
    if 'query' not in request.POST:
        return JsonResponse({'ok': False, 'error': 'No query field'})
    results = es.search(index='listing_index', body={'query':{'query_string':{'query': request.POST['query']}}, 'size':10})
    return JsonResponse({'ok':True, 'results': results['hits']})
