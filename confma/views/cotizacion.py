from django.shortcuts import render ,redirect , get_object_or_404
from django.http import Http404 , HttpResponse
# Models
from ..models import Cotizacion , Cloth
from ..forms.cotizacion import CotizacionFormModel
from django.views.generic import (CreateView, ListView,  DeleteView, UpdateView)

# Create your views here.

"""metodo que usa el LISTVIEW de django para lista todas las cotizaciones registrados
de las usando el metodo get_context_data para agregarle al context que se le pasa al template
el registro con todas las prendas registradas para asi asociar la informacion"""

class CotiListView(ListView):
    template_name = 'cotizacion/home.html'
    if Cloth.objects.all().filter(state = 1) == None:
        queryset = Cotizacion.objects.all().filter(state = 1)
    else:
        cloth = list(Cloth.objects.all())
        queryset = Cotizacion.objects.all().filter(state = 1 , cloth__in = cloth)

"""metodo que usa el CREATEVIEW de django para el registro de las cotizacion en la base de datos"""
class CotiCreateView(CreateView):
    template_name = "cotizacion/create.html"
    form_class = CotizacionFormModel
    # queryset = Cotizacion.objects.all()

    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../'

"""metodo que usa el UPDATEVIEW de django para la actulizacion de datos de las cotizacion"""
class CotiUpdateView(UpdateView):
    template_name = "cotizacion/update.html"
    form_class = CotizacionFormModel

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cotizacion , id=id_)

    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../../'

"""metodo que usa el DELETEVIEW de django para el borrado permanente de una cotizacion en particular
actualmente no se usa"""
class CotiDeleteView(DeleteView):
    template_name = 'cotizacion/delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cotizacion , id=id_)

    def get_success_url(self):
        return reverse('coti:coti_home')

"""
Metodo para el borrado logico del registro , cambia el estado del
registro de 1 a 0 
"""
def deletelog(request , id):
    obj = get_object_or_404 (Cotizacion , id=id)

    if request.method == 'POST':
        obj.state = 0
        obj.save()
        return redirect('../../')

    context = {
        'c' : obj
    }
    return render(request , 'cotizacion/deletel.html', context)

"""metodo que genera la vista para restaurar registro borrados logicamente"""
def restoreview(request):
    obj = Cotizacion.objects.all().filter(state = 0)
    context = {
        "coti" : obj,
        "model" : "Cotizacion",
    }

    return render(request , "cotizacion/restore.html" , context)

"""metodo que restaura los modelos borrados logicamente cambiando el estado de 0 a 1"""
def restore(request, id):
    obj = get_object_or_404(Cotizacion , id=id)
    if request.method == 'POST':
        obj.state = 1
        obj.save()
        return redirect('../../')
        
    response = 'I Dont Know <a href = "/confma/users/"> BACK </a>'
    return HttpResponse(response)
    