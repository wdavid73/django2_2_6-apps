from django.shortcuts import render ,redirect , get_object_or_404
from django.http import Http404 , HttpResponse
from django.urls import reverse
from django.views.generic import (CreateView ,UpdateView , ListView ,DeleteView)
# Models
from ..models import Client , Cloth , Cotizacion_Client , Cotizacion , Alquiler
#Forms
from ..forms.client import ClientFormModel

# Create your views here.

""" metodo que carga una vista con todos los clientes registrados filtrando
a los que tengan estado 0 para que no se muestren"""
def home(request , *args, **kwargs):
    # obj = Client.objects.all()
    obj = Client.objects.all().filter(state = 1)

    # clients = []
    # for client in obj:
    #     if client.state == 1:
    #         clients.append(client)
    
    context = {
        "clients" : obj,
        "model" : "Client"
     }
    return render(request , "clients/details.html" , context)

"""metodo que usa el CREATEVIEW de django para el registro de los
clientes en la base de datos"""
class ClientCreateView(CreateView):
    template_name = "clients/create.html"
    form_class = ClientFormModel
    # queryset = Client.objects.all()

    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../'

"""metodo que usa el LISTVIEW de django para mostrar una lista de los clientes
registrados , Actualmente no se usa"""
class ClientListView(ListView):
    template_name = 'clients/details.html'
    queryset = Client.objects.all().filter(state = 1)


"""metodo que usa el DELETEVIEW de django para borrar permanente un cliente en particular
actualmente no se Usa"""
class ClientDeleteView(DeleteView):
    template_name = 'clients/delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Client , id=id_)

    def get_success_url(self):
        return reverse('clients:clients_home')

"""metodo que usa el UPDATEVIEW de django para hacer actualizcion a los de los clientes"""
class ClientUpdateView(UpdateView):
    template_name = "clients/update.html"
    form_class = ClientFormModel

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Client , id=id_)

    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../../'

"""
Metodo para el borrado logico del registro , cambia el estado del
registro de 1 a 0 
"""
def deletelog(request , id):
    obj = get_object_or_404 (Client , id=id)

    if request.method == 'POST':
        obj.state = 0
        obj.save()
        return redirect('../../')

    context = {
        'client' : obj
    }
    return render(request , 'clients/deletel.html', context)

"""metodo que genera la vista para restaurar registro borrados logicamente"""
def restoreview(request):
    obj = Client.objects.filter(state = 0)
    return render(request , 'clients/restore.html', {'clients' : obj})
    
"""metodo que restaura los modelos borrados logicamente cambiando el estado de 0 a 1"""
def restore(request, id):
    obj = get_object_or_404(Client , id=id)
    if request.method == 'POST':
        obj.state = 1
        obj.save()
        return redirect('/confma')
        
    response = 'I Dont Know <a href = "/confma/clients/"> BACK </a>'
    return HttpResponse(response)

def search(request):
    ##tratar de implementar un formulario por django
    if request.method == 'POST':
        name = request.POST.get('name_client')
        number = request.POST.get('number_client')
        coti_cli = Cotizacion_Client.objects.all().filter(state = 1)
        if name != "" or number != "":

            obj_client = Client.objects.filter(state = 1).filter(name = name)
            cloth = coti_cloth()
            cotizacion = coti_client(obj_client)
            size_client = len(obj_client)
            alquileres = alqu_client_cloth(obj_client , cloth)
            context = { 'client' : obj_client , 'cloth' : cloth , 
                        'cotizacion' : cotizacion , 'size_client' : size_client , 'coti_client' : coti_cli , 'alquileres' : alquileres}
            return render(request, 'clients/search.html' , context)
        elif name == "" and number == "":
            message = "INGRESE INFORMACION EN LOS CAMPOS"
            obj_client = []
            size_client = len(obj_client)
            return render(request, 'clients/search.html' , { 'client' : obj_client , 'message' : message , 'size_client' : size_client})

    return render(request, 'clients/search.html' , {})

def tupla_coti_total(cotizacion , client):
    coti_client = Cotizacion_Client.objects.all().filter(state  = 1)
    COTI = []
    for cli in client:
        for coti in cotizacion:
            for cc in coti_client:
                if coti.id == cc.cotizacion_id and cc.client_id == cli.id :
                    COTI.append( (coti.id , cc.total) )
    return COTI

def alqu_client_cloth(client , cloth):
    alquileres = Alquiler.objects.all().filter(state = 1)
    array_alquiler = []
    obj_new = {}
    for alq in alquileres:
        for cli in client:
            for clo in cloth:
                    if alq.client_id == cli.id and alq.cloth_id == clo.id:
                        obj_new = { 
                            'alquiler_id' : alq.id , 
                            'alquiler_date_return' : alq.date_return,
                            'alquiler_date_now' : alq.date_now,
                            'alquiler_price' : alq.price,
                            'client_name' : cli.name , 
                            'client_lastname' : cli.lastname,
                            'cloth_name' : clo.name,
                            'cloth_color' : clo.color,
                            'cloth_size' : clo.size,
                            'cloth_fashion' : clo.fashion,
                            }
                        array_alquiler.append(obj_new)
    return array_alquiler

def coti_cloth():
    obj_coti = Cotizacion.objects.all().filter(state = 1)
    obj_cloth = Cloth.objects.all()
    cloth = []
    for coti in obj_coti:
        for clo in obj_cloth:
            if coti.cloth_id == clo.id:
                cloth.append(clo)
    return cloth

def coti_client(client):
    obj_client_coti = Cotizacion_Client.objects.all().filter( state = 1)
    obj_coti = Cotizacion.objects.all().filter(state = 1)
    cotizacion = []
    for cli in client:
        for cc in obj_client_coti:
            for coti in obj_coti:
                if cli.id == cc.client_id and coti.id == cc.cotizacion_id:
                    cotizacion.append(coti)
    return cotizacion