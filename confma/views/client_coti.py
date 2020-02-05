from django.shortcuts import render ,redirect , get_object_or_404
from django.http import Http404 , HttpResponse
# Models
from ..models import Cotizacion_Client , Cotizacion , Client , Cloth
from django.views.generic import (ListView)
#Forms
from ..forms.cotizacion_client import CUFormModel , Coti_UserFormModel


# Create your views here.
"""Metodo para el listado de todas las cotizacion asociadas a un client"""
class CCListView (ListView):
	template_name = 'cliente_cotizacion/list-client.html'
	queryset = Cotizacion_Client.objects.filter(state = 1)

"""
Segundo Metodo para el listado de todas las cotizacion asociadas a un client , en este
pasamos mas informacion asociada a la cotizacion en particular como a que cliente con su informacion , 
que prenda se cotizo y los valor de esa cotizacion.
"""
def list_view(request):
	obj_coti_clien = Cotizacion_Client.objects.all().filter(state = 1)
	obj_coti = Cotizacion.objects.all().filter(state = 1)
	obj_client = Client.objects.all().filter(state = 1)
	obj_cloth = Cloth.objects.all().filter(state = 1)

	context = {	
		"clients" : obj_client,
        "cotizacions" : obj_coti,
        "cotizacion_client" : obj_coti_clien,
        "cloth" : obj_cloth
	}
	return render(request , "cliente_cotizacion/list-client.html" , context)

"""
Metodo que Crea la vista para el registro de una cotizacion con un cliente
"""
def create_view(request, id):
	client = Client.objects.all().filter(state = 1)
	coti_obj = get_object_or_404(Cotizacion , id = id)
	total_coti = getTotal(coti_obj)
	cloth = get_cloth(coti_obj)
	context = {	
		'cliente' : client,
		'coti' : coti_obj,
		'total' : total_coti,
		'cloth' : cloth
	}
	return render(request , 'cliente_cotizacion/create.html' , context)


"""
Metodo para obtener una prenda en particular,
pasandole una cotizacion en especifico
"""
def get_cloth(coti_obj):
	obj_cloth = Cloth.objects.all().filter(state=1)
	for cloth in obj_cloth:
		if(cloth.id == coti_obj.cloth_id):
			return cloth

"""
Metodo que hace el registro en la base de datos obteniendo
y pasando los datos manualmente
"""
def create(request):
	q = request.POST.get('client_s')
	t = request.POST.get('total')
	coti_id = request.POST.get('coti_id')
	if request.method == "POST":
		total = float(t)
		if q != "":
			u_id = q
			Cotizacion_Client.objects.create( total = total , cotizacion_id = coti_id , client_id = u_id)
			return redirect("coti_client_list")
		else:
			u_id = 1
			Cotizacion_Client.objects.create( total = total , cotizacion_id = coti_id , client_id = u_id)
			return redirect("coti_client_list")
	else:
		return redirect("coti_list")

"""
Metodo para obtener el valor total de la cotizacion
"""
def getTotal(coti_obj):
	total1 = coti_obj.value_cloth + coti_obj.value_work
	total2 = coti_obj.value_threads + coti_obj.value_buttons 
	total3 = coti_obj.value_necks + coti_obj.value_embroidery + coti_obj.value_prints
	total = total1 + total2 + total3
	return total

"""
Metodo para el borrado logico del registro , cambia el estado del
registro de 1 a 0 
"""
def deletelog(request):	
	id_ = request.POST.get('coti_client_id')
	obj = get_object_or_404(Cotizacion_Client , id = id_)
	if request.method == 'POST':
		obj.state = 0
		obj.save()
		return redirect('coti_client_list')
		
"""metodo para obtener un cliente pasandole el modelo del cliente y el modelo
de cliente-cotizacion """
def get_client(client, obj):
	for cli in client:
		if cli.id == obj.client_id:
			return cli
"""metodo para obtener una cotizacion pasandole el modelo de cotizacion y el modelo
de cliente-cotizacion
"""
def get_cotizacion(cotizacion , obj):
	for coti in cotizacion:
		if coti.id == obj.cotizacion_id:
			return coti

"""metodo que genera la vista para restaurar registro borrados logicamente"""
def restore_view(request):
	obj_coti_clien = Cotizacion_Client.objects.all().filter(state=0)
	context = {	
        "cotizacion_client" : obj_coti_clien
	}
	return render(request , "cliente_cotizacion/restore.html" , context)
	
"""metodo que restaura los modelos borrados logicamente cambiando el estado de 0 a 1"""
def restore(request):
	id = request.POST.get('coti_user_id')
	obj = get_object_or_404(Cotizacion_Client , id = id)
	if request.method == 'POST':
		obj.state = 1 
		obj.save()
		return redirect('coti_client_list')