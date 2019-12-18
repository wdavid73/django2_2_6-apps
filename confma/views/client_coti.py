from django.shortcuts import render ,redirect , get_object_or_404
from django.http import Http404 , HttpResponse

# Models

from ..models import Cotizacion_Client , Cotizacion , Client , Cloth
from django.views.generic import (ListView)

#Forms
from ..forms.cotizacion_client import CUFormModel , Coti_UserFormModel

# Create your views here.

class UCListView (ListView):
	template_name = 'cliente_cotizacion/list-client.html'
	queryset = Cotizacion_Client.objects.all()

def list_view(request):
	obj_coti = Cotizacion.objects.all()
	obj_client = Client.objects.all()
	obj_coti_clien = Cotizacion_Client.objects.all()
	obj_cloth = Cloth.objects.all()
	context = {	
		"client" : obj_client,
        "cotizacion" : obj_coti,
        "cotizacion_user" : obj_coti_clien,
        "cloth" : obj_cloth
	}
	return render(request , "cliente_cotizacion/list-client.html" , context)

def create_view(request, id):
	u = Client.objects.all()
	coti_obj = get_object_or_404(Cotizacion , id = id)
	total_coti = getTotal(coti_obj)
	cloth = get_cloth(coti_obj)
	context = {	
		'cliente' : u,
		'coti' : coti_obj,
		'total' : total_coti,
		'cloth' : cloth
	}
	return render(request , 'cliente_cotizacion/create.html' , context)

def get_cloth(coti_obj):
	obj_cloth = Cloth.objects.all()
	for cloth in obj_cloth:
		if(cloth.id == coti_obj.cloth_id):
			return cloth


def create(request):
	q = request.POST.get('client_s')
	t = request.POST.get('total')
	coti_id = request.POST.get('coti_id')
	if request.method == "POST":
		total = float(t)
		if q != "":
			u_id = q
			Cotizacion_Client.objects.create( total = total , cotizacion_id = coti_id , client_id = u_id)
			return redirect("/confma/api/v1/cotizacion-client/list")
		else:
			u_id = 1
			Cotizacion_Client.objects.create( total = total , cotizacion_id = coti_id , client_id = u_id)
			return redirect("/confma/api/v1/cotizacion-client/list")
	else:
		return redirect("/confma/api/v1/cotizacion/list")

def getTotal(coti_obj):
	total1 = coti_obj.value_cloth + coti_obj.value_work
	total2 = coti_obj.value_threads + coti_obj.value_buttons 
	total3 = coti_obj.value_necks + coti_obj.value_embroidery + coti_obj.value_prints
	total = total1 + total2 + total3
	return total

def deletelog(request):	
	id = request.POST.get('coti_client_id')
	obj = get_object_or_404(Cotizacion_Client , id = id)
	obj_client = get_client(Client.objects.all() , obj)
	obj_cotizacion = get_cotizacion(Cotizacion.objects.all() ,obj)
	obj_cloth = get_cloth(obj_cotizacion)

	context = {
		'client_coti' : obj,
		'client' : obj_client,
		'cotizacion' : obj_cotizacion,
		'cloth':obj_cloth
	}

	return render (request , 'cliente_cotizacion/delete.html',context)

def temp(request):

	id = request.POST.get('coti_client_id')
	obj = get_object_or_404(Cotizacion_Client , id = id)
	if request.method == 'POST':
		obj.state = 0
		obj.save()
		return redirect('/confma')


def get_client(client, obj):
	for cli in client:
		if cli.id == obj.client_id:
			return cli

def get_cotizacion(cotizacion , obj):
	for coti in cotizacion:
		if coti.id == obj.cotizacion_id:
			return coti




def restore_view(request):
	obj_coti = Cotizacion.objects.all()
	obj_client = Client.objects.all()
	obj_coti_clien = Cotizacion_Client.objects.all()
	context = {	
		"client" : obj_client,
        "cotizacion" : obj_coti,
        "cotizacion_client" : obj_coti_clien
	}
	return render(request , "cliente_cotizacion/restore.html" , context)
	

def restore(request):
	id = request.POST.get('coti_user_id')
	obj = get_object_or_404(Cotizacion_Client , id = id)
	if request.method == 'POST':
		obj.state = 1 
		obj.save()
		return redirect('/confma/cotizacion-user/list')