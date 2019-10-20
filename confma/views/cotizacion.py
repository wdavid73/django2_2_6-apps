from django.shortcuts import render ,redirect , get_object_or_404
from django.http import Http404

# Models
from ..models import User , Cotizacion

# Create your views here.

def coti_view(request , *args, **kwargs):
    obj = Cotizacion.objects.all()
    context = {
        "coti" : obj,
        "model" : "Cotizacion"
     }
    return render(request , "cotizacion/home.html" , context)