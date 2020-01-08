from django.shortcuts import render ,redirect , get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404 , HttpResponse
from datetime import date

# Models
from ..models import Cloth , Alquiler , Client

def client_tupla(client_choice):
    if (Client.objects.all == None):
        return client_choice
    else:
        for cli in Client.objects.all():
            if cli.state == 1:
                client_choice.append((cli.id , (cli.name + " " + cli.lastname + " - " + cli.address + " - " + str(cli.phone) + " - " + str(cli.cellphone))))
        return client_choice

#Form
from ..forms.cloth import ClothFormModel 
from ..forms.alquiler import AlquilerFormModel
# Create your views here.
from django.views.generic import (CreateView ,UpdateView , ListView ,DeleteView)

"""metodo que usa el CREATEVIEW de django para el registro de las prendas en la base de datos"""
class ClothCreateView(CreateView):
    template_name = "cloth/create.html"
    form_class = ClothFormModel
    queryset = Cloth.objects.all()

    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../../../../'

"""metodo que usa el CREATEVIEW de django para el registro de los alquileres en la base de datos"""
class AlquilerCreateView(CreateView):
    template_name = "alquiler/create.html"
    form_class = AlquilerFormModel
    queryset = Alquiler.objects.all()

    def form_valid(self , form):
        # print(form.cleaned_data)
        now = date.today()
        if form.cleaned_data["date_return"] > now:
            if form.cleaned_data["client"].state == 1:
                return super().form_valid(form)
            else:
                return redirect('alquiler_create')   
        else:
            return redirect('alquiler_create')

    def get_success_url(self):
        return '../../../../'

"""metodo que usa el LISTVIEW de django para listar todas los alquileres registrados en la base de datos"""
class AlquilerListView(ListView):
     template_name = 'alquiler/details.html'
     queryset = Alquiler.objects.all()

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cloth_list'] = Cloth.objects.all()
        context['client_list'] = Client.objects.all()
        return context

"""metodo que renderiza las vista de index y home , una es la vista con el navbar para hacer CRUD en los distintos
modelos de la base de datos , pero antes se tienen que registrar o en su defecto iniciar sesion , y por otra parte el home
es la vista con el navbar en blanco con solo la opcion de ir al inicio o registrar o iniciar sesion"""
def home(request , *args , **kwargs):
    if request.user.is_authenticated:
        return render(request , "index.html" , {})
    else:
        return render(request , "home.html" , {})

"""metodo que renderiza la vista home , actualmente sin usar"""
def home_view(request , *args, **kwargs):
    return render(request , "home.html" , {})

"""metodo que renderiza la vista index , actualmente sin usar"""
def home_api(request , *args, **kwargs):
    
    return render(request , "index.html" , {})

"""metodo para mostrar una vista 404 en case de que se presente este error"""
def handler404(request, *args, **argv):
    response = render_to_response(
    			'404.html', {},
                context_instance=RequestContext(request))
    response.status_code = 404
    return response

"""metodo para mostrar una vista 500 en case de que se presente este error"""
def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response