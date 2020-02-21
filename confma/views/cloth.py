from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import (CreateView, ListView)

from ..forms.cloth import ClothFormModel
from ..models import Cloth, Alquiler
from ..static_methods import getTotal, getClothWithRental, getClothWithCotizacion


class ClothCreate(CreateView):
    template_name = "cloth/create.html"
    form_class = ClothFormModel

    def form_valid(self, form):
        print(form.cleaned_data['image'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('confma:list_all_cloth')


def UploadPhotoFashion(request):
    if request.method == 'POST':
        form = ClothFormModel(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            Cloth.objects.create(**form.cleaned_data)
            return redirect('confma:list_all_cloth')
    return redirect('confma:create_cloth')


class ListOfAllCloth(ListView):
    template_name = 'cloth/all_cloths.html'
    queryset = Cloth.objects.all().filter(state=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rentals'] = Alquiler.objects.all().filter(state=1)
        return context


def DetailsCloth(request, _id):
    cloth = get_object_or_404(Cloth, id=_id)
    cotizacion = getClothWithCotizacion(cloth)
    rental = getClothWithRental(cloth)
    total = getTotal(cotizacion)
    context = {
        'cloth': cloth,
        'cotizacion': cotizacion,
        'total': total,
        'rental': rental
    }
    return render(request, 'cloth/details.html', context)
