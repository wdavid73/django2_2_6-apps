from django.shortcuts import render ,redirect , get_object_or_404

# Models

from .models import User

#Forms

from .forms import UserForm

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


def user_create_view(request):
    form = UserForm(request.GET)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            #ingreso a la base de datos
            print(form.cleaned_data)
            User.objects.create(**form.cleaned_data)
            # form = UserForm()
            return redirect('../')
        else:
            print(form.errors)
            # error = form.errors

    context = {
        'form' : form
    }
    return render(request , "users/create.html" , context)

def user_details_view(request):
    obj = User.objects.all()
    context = {
        "user" : obj
    }
    return render(request , "users/details.html" , context)

def user_delete_view(request , id):
    obj = get_object_or_404(User , id = id)
    if request.method == "POST":
        obj.delete()
        print("listo pa borrar")
        return redirect('../../')
    context = {
        'user' : obj
    }

    return render(request , "users/delete.html" , context)


def user_update_view (request, id):
    obj = User.objects.get(id=id)
    print(obj)
    form = UserForm(request.GET)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            #User.objects.create(**form.cleaned_data)
    else:
        print(form.errors)
    #if form.is_valid():
    #    print("listo para actualizar")
        #form.save()
        #return redirec('../../')

    context = {
        'user' : obj,
    #    'form' : form
    }

    return render(request , "users/update.html" , context)

