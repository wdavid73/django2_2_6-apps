from django.shortcuts import render ,redirect , get_object_or_404
from django.http import Http404

# Models
from ..models import User , Cotizacion
from ..forms import CotizacionFormModel

# Create your views here.

def home(request , *args, **kwargs):
    obj = Cotizacion.objects.all()
    context = {
        "coti" : obj,
        "model" : "Cotizacion"
     }
    return render(request , "cotizacion/home.html" , context)

def create(request , id):
	obj = get_object_or_404(User , id=id)
	form = CotizacionFormModel(request.GET)
	print("paso")
	if request.method == "POST":
		print("paso")
		form = CotizacionFormModel(request.POST)
		if form.is_valid():
			print("paso")
			print(form.cleaned_data)
			Cotizacion.objects.create(**form.cleaned_data)
		else:
			print(form.errors)
	context = {

		'form' : form,
		'user' : obj
	}
	return render(request, "cotizacion/create.html" , context)


# def create(request):
#     form = UserForm(request.GET)
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             #ingreso a la base de datos
#             print(form.cleaned_data)
#             User.objects.create(**form.cleaned_data)
#             # form = UserForm()
#             return redirect('../')
#         else:
#             print(form.errors)
#             # error = form.errors

#     context = {
#         'form' : form
#     }
#     return render(request , "users/create.html" , context)

# def deletelog(request , id):
#     obj = get_object_or_404 (User , id=id)

#     if request.method == 'POST':
#         obj.state = 0
#         obj.save()
#         return redirect('../../')

#     context = {
#         'user' : obj
#     }
#     return render(request , 'users/deletel.html', context)
