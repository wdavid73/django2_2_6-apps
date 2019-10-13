from django.shortcuts import render

# Models

from .models import User

# Create your views here.

def home_view(request , *args, **kwargs):
    context = {}
    return render(request , "home.html" , context)

def user_view(request , *args, **kwargs):
    obj = User.objects.all()
    context = {
        "user" : obj,
        "model" : "Users"
     }
    return render(request , "users/home_users.html" , context)

def user_details_view(request):
    obj = User.objects.all()
    context = {
        "user" : obj
    }
    return render(request , "users/details.html" , context)
