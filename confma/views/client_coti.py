from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import (ListView , CreateView)
from .general import PossibleError
from ..models import CotizacionClient, Cotizacion, Client, Cloth
from ..forms.clientcotizacion import CotizacionClientForm



class ListOfAllClientsAndCotizacion(ListView):
    template_name = 'cliente_cotizacion/list.html'
    queryset = CotizacionClient.objects.filter(state=1)


def ClientCotizacionView(request, id_):
    form = CotizacionClientForm
    cotizacion = get_object_or_404(Cotizacion, id=id_)
    client = Client.objects.all().filter(state=1)
    total = getTotal(cotizacion)
    context = {
        'form' : form,
        'cliente': client,
        'cotizacion': cotizacion,
        'total': total
    }
    return render(request, 'cliente_cotizacion/create.html', context)


class CreateClientCotizacion(CreateView):
    model = CotizacionClient
    template_name = "cliente_cotizacion/create.html"
    form_class = CotizacionClientForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('confma:list_of_all_cotizacion_client')


def DeleteClientCotizacion(request):
    _id = request.POST.get('coti_client_id')
    client_cotizacion_obj = get_object_or_404(CotizacionClient, id=_id)
    if request.method == 'POST':
        client_cotizacion_obj.state = 0
        client_cotizacion_obj.save()
        return redirect('confma:list_of_all_cotizacion_client')


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

    message: "Error Restaurando el registro de un Cliente junto con su Cotizacion"
    situation: "Restauracion de Cliente Cotizacion"
    return PossibleError(request, message, situation)


def getTotal(cotizacion):
    total1 = cotizacion.value_cloth + cotizacion.value_work
    total2 = cotizacion.value_threads + cotizacion.value_buttons
    total3 = cotizacion.value_necks + cotizacion.value_embroidery + cotizacion.value_prints
    total  = total1 + total2 + total3
    return total


def getClient(client, obj):
    for cli in client:
        if cli.id == obj.client_id:
            return cli


def getCotizacion(cotizacion, obj):
    for coti in cotizacion:
        if coti.id == obj.cotizacion_id:
            return coti

def get_cloth(cotizacion):
    cloth_obj = Cloth.objects.all().filter(state=1)
    for cloth in cloth_obj:
        if cloth.id == cotizacion.cloth_id:
            return cloth
