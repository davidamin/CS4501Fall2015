from django.shortcuts import render,render_to_response, get_object_or_404
from django.template import Context, RequestContext, loader
from django.template.loader import get_template
from django.http import HttpResponse
from django.http import JsonResponse
import json
import requests

def home(request):
	return render_to_response("main.html", context_instance=RequestContext(request))
