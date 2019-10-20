from django.shortcuts import render ,redirect , get_object_or_404

# Models
from .models import User , Cotizacion

#Forms
from .forms import UserForm , UserFormModel

# Create your views here.
from django.views.generic import (UpdateView)

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
<<<<<<< HEAD:confma/views_try.py
        return '../../'
=======
        return '../../'



# def user_update_view(request , *args , **kwargs):
#     obj = User.objects.get(id=27)
#     form = UserForm(request.POST or None , instance=obj)

#     if form.is_valid():
#         print("actu")

#     context = {
#         'form' : form
#     }

#     return render(request , "users/update.html" , context)


# Update base method
# def product_create_view (request):
#     #form = ProductForm(request.POST or None)

#     #forma para traer un registro de la base de datos y mostrar en un formulario para su edicion
#     obj = Product.objects.get(id=1)
#     form = ProductForm(request.POST or None , instance = obj)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form' : form
#     }

#     return render(request, "product/product_create.html" ,context)



def coti_view(request , *args, **kwargs):
    obj = Cotizacion.objects.all()
    context = {
        "coti" : obj,
        "model" : "Cotizacion"
     }
    return render(request , "cotizacion/home.html" , context)
>>>>>>> confma:confma/views.py
