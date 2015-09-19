from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from first import models
from django.core import serializers

def index(request):
    return HttpResponse("Hello World!")

def add_vehicle(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be POST'})
    new_car = models.Vehicle()
    if 'max_seats' in request.POST:
        new_car.max_seats = request.POST['max_seats']
    if 'trunk_space' in request.POST:
        new_car.trunk_space = request.POST['trunk_space']
    if 'notes' in request.POST:
        new_car.notes = request.POST['notes']
    if 'make' in request.POST:
        new_car.make = request.POST['make']
    if 'model' in request.POST:
        new_car.model = request.POST['model']
    if 'year' in request.POST:
        new_car.year = request.POST['year']
    if 'color' in request.POST:
        new_car.color = request.POST['color']
    if 'plates' in request.POST:
        new_car.plates = request.POST['plates']
    if 'uninsured' in request.POST:
        new_car.uninsured = request.POST['uninsured']
    if 'road_assistance' in request.POST:
        new_car.road_assistance = request.POST['road_assistance']
    if 'accomodations' in request.POST:
        new_car.accomodations = request.POST['accomodations']
    new_car.save()
    return JsonResponse({'ok':True, 'log': 'Added vehicle'})

def car_list(request):
    cars = models.Vehicle.objects.all()
    formatted = [str(c.id) + str(c.make) + str(c.model) + '\n' for c in cars]
    return JsonResponse(serializers.serialize("json", models.Vehicle.objects.all()),safe=False)

def get_car(request, car):
    if request.method != 'GET':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be get'})
    try:
        v = models.Vehicle.objects.get(pk=car)
    except models.Vehicle.DoesNotExist:
        return JsonResponse({'ok': False, 'error': 'Failed to find car id ' + car})
    ret_val = serializers.serialize('json',[v,])
    return JsonResponse({'ok':True,'car':ret_val})

def update_car(request, car):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be POST'})
    
    try:
        this_car = models.Vehicle.objects.get(pk=car)
    except:
        return JsonResponse({'ok': False, 'error': 'Failed to find car id ' + car})

    if 'max_seats' in request.POST:
        this_car.max_seats = request.POST['max_seats']
    if 'trunk_space' in request.POST:
        this_car.trunk_space = request.POST['trunk_space']
    if 'notes' in request.POST:
        this_car.notes = request.POST['notes']
    if 'make' in request.POST:
        this_car.make = request.POST['make']
    if 'model' in request.POST:
        this_car.model = request.POST['model']
    if 'year' in request.POST:
        this_car.year = request.POST['year']
    if 'color' in request.POST:
        this_car.color = request.POST['color']
    if 'plates' in request.POST:
        this_car.plates = request.POST['plates']
    if 'uninsured' in request.POST:
        this_car.uninsured = request.POST['uninsured']
    if 'road_assistance' in request.POST:
        this_car.road_assistance = request.POST['road_assistance']
    if 'accomodations' in request.POST:
        this_car.accomodations = request.POST['accomodations']
    this_car.save()
    return JsonResponse({'ok':True, 'log': 'Updated vehicle ' + car})

def create_user(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be post'})
    else :
        return JsonResponse({'ok':True, 'log': 'User Created'})

def edit_user(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be post'})
    else :
        return JsonResponse({'ok':True, 'log': 'User Info Editted'})

def deactivate_user(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be post'})
    else :
        return JsonResponse({'ok':True, 'log': 'User Account Deactivated'})
