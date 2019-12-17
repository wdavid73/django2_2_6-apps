from django.shortcuts import render ,redirect , get_object_or_404 , render_to_response
from django.http import HttpResponse
# Create your views here.
from django.views.generic import (ListView)


def index(request , *args, **kwargs):
    return render(request , "index_project.html" , {})
