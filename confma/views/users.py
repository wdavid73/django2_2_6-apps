from django.shortcuts import render ,redirect , get_object_or_404
from django.http import Http404
# Models
from ..models import User

#Forms
from ..forms import UserForm , UserFormModel

# Create your views here.
from django.views.generic import (UpdateView)

def home(request , *args, **kwargs):
    obj = User.objects.all()
    context = {
        "user" : obj,
        "model" : "Users"
     }
    return render(request , "users/home_users.html" , context)

  
def create(request):
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

def details(request):
    obj = User.objects.all()
    context = {
        "user" : obj
    }
    return render(request , "users/details.html" , context)

def delete(request , id):
    obj = get_object_or_404(User , id = id)
    if request.method == "POST":
        obj.delete()
        print("listo pa borrar")
        return redirect('../../')
    context = {
        'user' : obj
    }

    return render(request , "users/delete.html" , context)


class UserUpdateView(UpdateView):
    template_name = "users/update.html"
    form_class = UserFormModel

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User , id=id_)

    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../../'

def deletelog(request , id):
    obj = get_object_or_404 (User , id=id)

    if request.method == 'POST':
        obj.state = 0
        obj.save()
        return redirect('../../')

    context = {
        'user' : obj
    }
    return render(request , 'users/deletel.html', context)


# def restore(request , id):
#     obj = get_object_or_404 (User , id=id)

#     if request.method == 'POST':
#         obj.state = 1
#         obj.save()
#         return redirect('../../')

#     context = {
#         'user' : obj
#     }
#     return render(request , 'users/template_name.html', context)
