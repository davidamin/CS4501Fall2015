from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello World!")
# Create your views here.

def add_vehicle(request):
    if request.method != 'GET':
        return JsonResponse({'ok': False, 'error': 'Wrong request type, should be get'})
    return JsonResponse({'ok':True, 'log': 'Added vehicle'})
