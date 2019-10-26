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
        "model" : "Cotizacion",
    }

    return render(request , "cotizacion/home.html" , context)

def create(request):
	form = CotizacionFormModel(request.GET)
	if request.method == "POST":
		form = CotizacionFormModel(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			Cotizacion.objects.create(**form.cleaned_data)
			return redirect('../')
		else:
			print(form.errors)

	context = {
		'form' : form
	}
	return render(request, "cotizacion/create.html" , context)

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
