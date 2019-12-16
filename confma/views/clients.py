from django.shortcuts import render ,redirect , get_object_or_404
from django.http import Http404 , HttpResponse
from django.urls import reverse

# Models
from ..models import Client

#Forms
from ..forms.client import ClientFormModel

# Create your views here.
from django.views.generic import (CreateView ,UpdateView , ListView ,DeleteView)

def home(request , *args, **kwargs):
    obj = Client.objects.all()

    clients = []
    for client in obj:
        if client.state == 1:
            clients.append(client)
    
    context = {
        "client" : clients,
        "model" : "Client"
     }
    return render(request , "clients/home_clients.html" , context)


class ClientCreateView(CreateView):
    template_name = "clients/create.html"
    form_class = ClientFormModel
    queryset = Client.objects.all()

    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../'

def details(request):
    obj = Client.objects.all()
    context = {
        "client" : obj
    }
    return render(request , "clients/details.html" , context)

class ClientListView(ListView):
    template_name = 'clients/details.html'
    queryset = Client.objects.all()



class ClientDeleteView(DeleteView):
    template_name = 'clients/delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Client , id=id_)

    def get_success_url(self):
        return reverse('clients:clients_home')


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


def restoreview(request):
    obj = Client.objects.all()
    context = {
        'clients' : obj
    }
    return render(request , 'clients/restore.html', context)

def restore(request, id):
    obj = get_object_or_404(Client , id=id)
    if request.method == 'POST':
        obj.state = 1
        obj.save()
        return redirect('../../')
        
    response = 'I Dont Know <a href = "/confma/clients/"> BACK </a>'
    return HttpResponse(response)
    
