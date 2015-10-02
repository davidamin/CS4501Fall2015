from django.shortcuts import render,render_to_response, get_object_or_404
from django.template import Context, RequestContext, loader
from django.template.loader import get_template

# Create your views here.

def custom_processor(request):
    return {
        "first": "dave",
        "last": "amin",
    }

def view_normal(request):
    return render_to_response("main.html", {"unique_message": "Specific to a template"},
    context_instance=RequestContext(request, processors=[custom_processor]))
