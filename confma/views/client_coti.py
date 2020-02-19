from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import (ListView, CreateView)

from .general import PossibleError, getTotal
from ..forms.clientcotizacion import CotizacionClientForm
from ..models import CotizacionClient, Cotizacion, Client


class ListOfAllClientsAndCotizacion(ListView):
    template_name = 'cliente_cotizacion/list.html'
    queryset = CotizacionClient.objects.filter(state=1)


def ClientCotizacionView(request, id_):
    form = CotizacionClientForm
    cotizacion = get_object_or_404(Cotizacion, id=id_)
    client = Client.objects.all().filter(state=1)
    total = getTotal(cotizacion)
    context = {
        'form': form,
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
