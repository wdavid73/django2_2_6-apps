from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse ,HttpResponseForbidden
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Models
from ..models import Cloth, Alquiler, Client
# Form
from ..forms.cloth import ClothFormModel
from ..forms.alquiler import AlquilerFormModel
# Create your views here.
from django.views.generic import (CreateView, UpdateView, ListView, DeleteView)



"""metodo que usa el CREATEVIEW de django para el registro de las prendas en la base de datos"""


class ClothCreateView(CreateView):
    template_name = "cloth/create.html"
    form_class = ClothFormModel

    # queryset = Cloth.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data['image'])
        return super().form_valid(form)

    def get_success_url():
        return '../../../../'


def upload_pic(request):
    print(request.FILES)
    if request.method == 'POST':
        form = ClothFormModel(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            Cloth.objects.create(**form.cleaned_data)
            return redirect('../list')
    return redirect('cloth_create')

class ClothListView(ListView):
    template_name = 'cloth/photos.html'
    queryset = Cloth.objects.all().filter(state = 1)


"""metodo que usa el CREATEVIEW de django para el registro de los alquileres en la base de datos"""


class AlquilerCreateView(CreateView):
    template_name = "alquiler/create.html"
    form_class = AlquilerFormModel

    # queryset = Alquiler.objects.all()

    def form_valid(self, form):
        # print(form.cleaned_data)
        now = date.today()
        if form.cleaned_data["date_return"] > now:
            if form.cleaned_data["client"].state == 1:
                return super().form_valid(form)
            else:
                return redirect('alquiler_create')
        else:
            return redirect('alquiler_create')

    def get_success_url():
        return '../../../../'


"""metodo que usa el LISTVIEW de django para listar todas los alquileres registrados en la base de datos"""


class AlquilerListView(ListView):
    template_name = 'alquiler/details.html'
    if not Client.DoesNotExist:
        list_client = list(Client.objects.all().filter(state=1))
        queryset = Alquiler.objects.filter(state=1).filter(client__in=list_client)
    else:
        queryset = Alquiler.objects.filter(state=1)
        

"""metodo que renderiza las vista de index y home , una es la vista con el navbar para hacer CRUD en los distintos
modelos de la base de datos , pero antes se tienen que registrar o en su defecto iniciar sesion , y por otra parte el home
es la vista con el navbar en blanco con solo la opcion de ir al inicio o registrar o iniciar sesion"""


def home(request, *args, **kwargs):
    if request.user.is_authenticated:
        if Cloth.objects.all().filter(state=1) is None:
            return render(request, "index.html", {})
        else:
            cloth = Cloth.objects.all().filter(state=1)
            return render(request, "index.html", {'cloth': cloth})
    else:
        return render(request, "home.html", {})


""" metodo que renderiza la vista home , actualmente sin usar """


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


"""metodo que renderiza la vista index , actualmente sin usar"""


def home_api(request, *args, **kwargs):
    return render(request, "index.html", {})


"""metodo para mostrar una vista 404 en case de que se presente este error"""


def handler404(request, *args, **argv):
    response = render_to_response(
        '404.html', {})
    response.status_code = 404
    return response


"""metodo para mostrar una vista 500 en case de que se presente este error"""


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response


def client_tupla(client_choice):
    if Client.objects.all is None:
        return client_choice
    else:
        for cli in Client.objects.all():
            if cli.state == 1:
                client_choice.append((cli.id, (
                        cli.name + " " + cli.lastname + " - " + cli.address + " - " + str(cli.phone) + " - " + str(
                    cli.cellphone))))
        return client_choice
