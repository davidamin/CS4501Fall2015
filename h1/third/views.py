from django.shortcuts import render,render_to_response, get_object_or_404
from django.template import Context, RequestContext, loader
from django.template.loader import get_template
from django.http import HttpResponse
from django.http import JsonResponse
import json
import requests

# Create your views here.

def custom_processor(request):
    r = requests.get('http://exp-api:8000/exp/ride_detail')
    return {
        "first": json.loads(r.text)['data'],
        "last": "amin",
    }

def view_normal(request):
    return render_to_response("main.html", {"unique_message": "Specific to a template"},
    context_instance=RequestContext(request, processors=[custom_processor]))
