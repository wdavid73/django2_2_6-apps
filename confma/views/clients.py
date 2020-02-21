from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import (CreateView, UpdateView, ListView, DeleteView)

from ..forms.client import ClientForm, FindForm
from ..models import Client, Alquiler, CotizacionClient
from ..static_methods import getClientWithRental, getClientWithCotizacion, PossibleError


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
    form = FindForm
    clients = Client.objects.all().filter(state=1)

    if request.method == 'POST':
        form = FindForm(request.POST)

        if form.is_valid():
            client = form.cleaned_data['client']
            rental = getClientWithRental(Alquiler, client)
            cotizacion = getClientWithCotizacion(CotizacionClient, client)
            context = {
                'client': client,
                'rentals': rental,
                'cotizaciones': cotizacion,
                'count_rental': rental.count(),
                'count_coti': cotizacion.count(),
                'form': form
            }
            return render(request, 'clients/find.html', context)
    return render(request, 'clients/find.html', {'form': form})
