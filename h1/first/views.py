from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from first import models

def index(request):
    return HttpResponse("Hello World!")
# Create your views here.

def add_vehicle(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be POST'})
    new_car = models.Vehicle()
    #new_car.save()
    if 'max_seats' in request.POST:
        new_car.max_seats = request.POST['max_seats']
    new_car.save()
    return JsonResponse({'ok':True, 'log': 'Added vehicle'})
