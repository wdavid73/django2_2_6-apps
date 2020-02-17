from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import (CreateView, ListView, DeleteView, UpdateView)

from .general import PossibleError
from ..forms.cotizacion import CotizacionFormModel
from ..models import Cotizacion, Cloth


def getCotizacionWithCloth(Cotizacion, Cloth):
    cloth = list(Cloth.objects.all())
    queryset = Cotizacion.objects.all().filter(state=1, cloth__in=cloth)
    return queryset


class ListAllCotizacionByCloth(ListView):
    template_name = 'cotizacion/home.html'
    if not Cloth.DoesNotExist:
        queryset = getCotizacionWithCloth(Cotizacion, Cloth)
    else:
        queryset = Cotizacion.objects.all().filter(state=1)


class CreateCotizacion(CreateView):
    template_name = "cotizacion/create.html"
    form_class = CotizacionFormModel

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('confma:list_of_all_cotizaciones')


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
        return reverse('confma:list_of_all_cotizaciones')


class DeleteCotizacionPermanentById(DeleteView):
    template_name = 'cotizacion/delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cotizacion, id=id_)

    def get_success_url(self):
        return reverse('confma:list_of_all_cotizaciones')


def DeleteCotizacion(request, id):
    cotizacion = get_object_or_404(Cotizacion, id=id)

    if request.method == 'POST':
        cotizacion.state = 0
        cotizacion.save()
        return redirect('confma:list_of_all_cotizaciones')

    context = {
        'cotizacion': cotizacion
    }
    return render(request, 'cotizacion/delete.html', context)


def RestoreCotizacionView(request):
    cotizaciones = Cotizacion.objects.all().filter(state=0)
    context = {
        "cotizaciones": cotizaciones,
    }

    return render(request, "cotizacion/restore.html", context)


def RestoreCotizacionById(request, id):
    obj = get_object_or_404(Cotizacion, id=id)
    if request.method == 'POST':
        obj.state = 1
        obj.save()
        return redirect('confma:list_of_all_cotizaciones')

    message: "Error Restaurando el registro de una Cotizacion sin Cliente"
    situation: "Restauracion de Cotizacion"
    return PossibleError(request, message, situation)
