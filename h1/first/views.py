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