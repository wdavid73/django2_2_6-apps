from django.shortcuts import render ,redirect , get_object_or_404
from django.http import Http404 , HttpResponse

# Models

from ..models import Cotizacion_User , Cotizacion , User
from django.views.generic import (ListView)

#Forms
from ..forms.cotizacion_user import CUFormModel , Coti_UserFormModel

# Create your views here.

class UCListView (ListView):
	template_name = 'cliente_cotizacion/list-client.html'
	queryset = Cotizacion_User.objects.all()

def list_view(request):
	obj_coti = Cotizacion.objects.all()
	obj_user = User.objects.all()
	obj_coti_user = Cotizacion_User.objects.all()
	context = {	
		"user" : obj_user,
        "cotizacion" : obj_coti,
        "cotizacion_user" : obj_coti_user
	}
	return render(request , "cliente_cotizacion/list-client.html" , context)

def create_view(request, id):
	u = User.objects.all()
	coti_obj = get_object_or_404(Cotizacion , id = id)
	total_coti = getTotal(coti_obj)
	context = {	
		'cliente' : u,
		'coti' : coti_obj,
		'total' : total_coti
	}
	return render(request , 'cliente_cotizacion/create.html' , context)


def create(request):
	q = request.POST.get('client_s')
	t = request.POST.get('total')
	coti_id = request.POST.get('coti_id')
	if request.method == "POST":
		total = float(t)
		if q != "":
			u_id = q
			Cotizacion_User.objects.create( total = total , cotizacion_id = coti_id , user_id = u_id)
			return redirect('../')
		else:
			u_id = 1
			Cotizacion_User.objects.create( total = total , cotizacion_id = coti_id , user_id = u_id)
			return redirect('../')
	else:
		return redirect("/confma/cotizacion/list")

def getTotal(coti_obj):
	total1 = coti_obj.value_cloth + coti_obj.value_work
	total2 = coti_obj.value_threads + coti_obj.value_buttons 
	total3 = coti_obj.value_necks + coti_obj.value_embroidery + coti_obj.value_prints
	total = total1 + total2 + total3
	return total

# def restore(request, id):
#     obj = get_object_or_404(User , id=id)
#     if request.method == 'POST':
#         obj.state = 1
#         obj.save()
#         return redirect('../../')
        
#     response = 'I Dont Know <a href = "/confma/users/"> BACK </a>'
#     return HttpResponse(response)






