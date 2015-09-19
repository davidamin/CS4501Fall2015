from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from first import models
from django.core import serializers

def index(request):
    return HttpResponse("Hello World!")
# Create your views here.

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
    new_car.save()
    return JsonResponse({'ok':True, 'log': 'Added vehicle'})

def car_list(request):
    cars = models.Vehicle.objects.all()
    formatted = [str(c.id) + str(c.make) + str(c.model) + '\n' for c in cars]
    return JsonResponse(serializers.serialize("json", models.Vehicle.objects.all()),safe=False)

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
