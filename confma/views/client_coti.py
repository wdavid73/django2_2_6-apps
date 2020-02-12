from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
# Models
from ..models import CotizacionClient, Cotizacion, Client, Cloth
from django.views.generic import (ListView)


# Forms

# Create your views here.

class ListOfAllClientsAndCotizacion(ListView):
    template_name = 'cliente_cotizacion/list.html'
    queryset = CotizacionClient.objects.filter(state=1)


def ClientCotizacionView(request, id):
    cotizacion_obj = get_object_or_404(Cotizacion, id=id)
    client = Client.objects.all().filter(state=1)
    total_cotizacion = getTotal(cotizacion_obj)
    cloth = get_cloth(cotizacion_obj)
    context = {
        'cliente': client,
        'coti': cotizacion_obj,
        'total': total_cotizacion,
        'cloth': cloth
    }
    return render(request, 'cliente_cotizacion/create.html', context)


def get_cloth(cotizacion):
    cloth_obj = Cloth.objects.all().filter(state=1)
    for cloth in cloth_obj:
        if cloth.id == cotizacion.cloth_id:
            return cloth


def create(request):
    client_id = request.POST.get('client_s')
    total_cotizacion = request.POST.get('total')
    cotizacion_id = request.POST.get('coti_id')
    if request.method == "POST":
        total = float(total_cotizacion)
        if client_id != "":
            _id_client = client_id
            CotizacionClient.objects.create(total=total, cotizacion_id=cotizacion_id, client_id=_id_client)
            return redirect("confma:list_of_all_cotizacion_client")
        else:
            _id_client = 1
            CotizacionClient.objects.create(total=total, cotizacion_id=cotizacion_id, client_id=_id_client)
            return redirect("confma:list_of_all_cotizacion_client")
    else:
        return redirect("confma:list_of_all_cotizacion_client")


def getTotal(cotizacion_obj):
    total1 = cotizacion_obj.value_cloth + cotizacion_obj.value_work
    total2 = cotizacion_obj.value_threads + cotizacion_obj.value_buttons
    total3 = cotizacion_obj.value_necks + cotizacion_obj.value_embroidery + cotizacion_obj.value_prints
    total = total1 + total2 + total3
    return total


def DeleteClientCotizacion(request):
    _id = request.POST.get('coti_client_id')
    client_cotizacion_obj = get_object_or_404(CotizacionClient, id=_id)
    if request.method == 'POST':
        client_cotizacion_obj.state = 0
        client_cotizacion_obj.save()
        return redirect('confma:list_of_all_cotizacion_client')


def getClient(client, obj):
    for cli in client:
        if cli.id == obj.client_id:
            return cli


def getCotizacion(cotizacion, obj):
    for coti in cotizacion:
        if coti.id == obj.cotizacion_id:
            return coti


def RestoreClientCotizacionView(request):
    client_cotizacion_obj = CotizacionClient.objects.all().filter(state=0)
    context = {
        "cotizacion_client": client_cotizacion_obj
    }
    return render(request, "cliente_cotizacion/restore.html", context)


def RestoreClientCotizacion(request):
    _id = request.POST.get('coti_user_id')
    cotizacion_client_obj = get_object_or_404(CotizacionClient, id=_id)
    if request.method == 'POST':
        cotizacion_client_obj.state = 1
        cotizacion_client_obj.save()
        return redirect('confma:list_of_all_cotizacion_client')
