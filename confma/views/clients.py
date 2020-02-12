from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import (CreateView, UpdateView, ListView, DeleteView)

from ..forms.client import ClientForm
from ..models import Client, Cloth, CotizacionClient, Cotizacion, Alquiler
from ..views.general import PossibleError


def ListAllClients(request):
    clients = Client.objects.all().filter(state=1)
    context = {
        "clients": clients,
        "model": "Client"
    }
    return render(request, "clients/details.html", context)


class CreateClient(CreateView):
    model = Client
    template_name = "clients/create.html"
    form_class = ClientForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('confma:list_all_clients')


class ListOfClients(ListView):
    template_name = 'clients/details.html'
    queryset = Client.objects.all().filter(state=1)


class DeleteClientPermanent(DeleteView):
    template_name = 'clients/delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Client, id=id_)

    def get_success_url(self):
        return reverse('confma:list_all_clients')


class UpdateClient(UpdateView):
    template_name = "clients/update.html"
    form_class = ClientForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Client, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('confma:list_all_clients')


def DeleteClient(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        client.state = 0
        client.save()
        return redirect('confma:list_all_clients')
    context = {'client': client}

    return render(request, 'clients/delete.html', context)


def RestoreClientView(request):
    clients = Client.objects.all().filter(state=0)
    return render(request, 'clients/restore.html', {'clients': clients})


def RestoreClient(request, id):
    obj = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        obj.state = 1
        obj.save()
        return redirect('confma:list_all_clients')

    message: "Error Restaurando Cliente"
    situation: "Restauracion de Usuario"
    return PossibleError(request, message, situation)


def FindClient(request):
    ##tratar de implementar un formulario por django
    clients = Client.objects.all().filter(state=1)

    if request.method == 'POST':
        id_ = request.POST.get('client_id')
        obj_client = get_object_or_404(Client, id=id_)
        # query que trate los alquileres de un cliente en especifico
        alquiler_cliente = Alquiler.objects.filter(client=obj_client)
        count_alquiler = alquiler_cliente.count()
        cloth = list(Cloth.objects.all().filter(state=1))  # array con los registro de todas las prendas
        # trae las cotizacion que ya tiene una prenda asignada
        cotizacion = list(Cotizacion.objects.all().filter(state=1, cloth__in=cloth))
        # trae los registro de los clientes que tienen asignado una cotizacion con su respectiva prenda
        cotizacion_cliente = CotizacionClient.objects.filter(cotizacion__in=cotizacion, client=obj_client)
        count_coti_cli = cotizacion_cliente.count()
        context = {
            'all_client': clients,
            'alquiler_cliente': alquiler_cliente,
            'count_alquiler': count_alquiler,
            'cotizacion_client': cotizacion_cliente,
            'count_coti_cli': count_coti_cli,
            'client': obj_client
        }
        return render(request, 'clients/search.html', context)

    return render(request, 'clients/search.html', {'all_client': clients})
