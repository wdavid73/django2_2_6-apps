from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
# Models
from ..models import Cotizacion, Cloth
from ..forms.cotizacion import CotizacionFormModel
from django.views.generic import (CreateView, ListView, DeleteView, UpdateView)


# Create your views here.

class ListAllCotizacionByCloth(ListView):
    template_name = 'cotizacion/home.html'
    if not Cloth.DoesNotExist:
        cloth = list(Cloth.objects.all())
        queryset = Cotizacion.objects.all().filter(state=1, cloth__in=cloth)
    else:
        queryset = Cotizacion.objects.all().filter(state=1)


class CreateCotizacion(CreateView):
    template_name = "cotizacion/create.html"
    form_class = CotizacionFormModel

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../'


class UpdateCotizacionById(UpdateView):
    template_name = "cotizacion/update.html"
    form_class = CotizacionFormModel

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cotizacion, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../../'


class DeleteCotizacionPermanentById(DeleteView):
    template_name = 'cotizacion/delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cotizacion, id=id_)

    def get_success_url(self):
        return reverse('coti:coti_home')


def DeleteCotizacion(request, id):
    obj = get_object_or_404(Cotizacion, id=id)

    if request.method == 'POST':
        obj.state = 0
        obj.save()
        return redirect('../../')

    context = {
        'c': obj
    }
    return render(request, 'cotizacion/delete.html', context)


def RestoreCotizacionView(request):
    cotizacion = Cotizacion.objects.all().filter(state=0)
    context = {
        "coti": cotizacion,
        "model": "Cotizacion",
    }

    return render(request, "cotizacion/restore.html", context)


def RestoreCotizacionById(request, id):
    obj = get_object_or_404(Cotizacion, id=id)
    if request.method == 'POST':
        obj.state = 1
        obj.save()
        return redirect('../../')

    response = 'I Dont Know <a href = "/confma/users/"> BACK </a>'
    return HttpResponse(response)
