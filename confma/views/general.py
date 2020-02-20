from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import render_to_response
from django.views.generic import (CreateView, ListView)

from ..forms.client import FindForm
from ..forms.cloth import ClothFormModel
from ..models import Cloth, Alquiler, Client, CotizacionClient, Cotizacion


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


def ClothIfRental(Cloth, Alquiler):
    cloth = Cloth.objects.all().filter(state=1)
    for clo in cloth:
        rental = Alquiler.objects.all().get(cloth_id=clo.id)
        print(rental)


class ListOfAllCloth(ListView):
    template_name = 'cloth/all_cloths.html'
    queryset = Cloth.objects.all().filter(state=1)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['rentals'] = Alquiler.objects.all().filter(state=1)
        return context


def HomePage(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, "index.html", {})
    else:
        return render(request, "home.html", {})


def PossibleError(request, message, situation):
    return render(request, 'Error.html', {'message': message, 'situation': situation})


def handler404(request, *args, **argv):
    response = render_to_response(
        '404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response


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


def RedirectFind(request):
    if request.path == '/confma/api/v1/clients/search/':
        return FindClient(request)

    return HttpResponse('find general')


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


def getClientWithRental(Alquiler, _client):
    rental = Alquiler.objects.all().filter(state=1, client=_client)
    return rental


def getClientWithCotizacion(CotizacionClient, client):
    cotizacion_client = CotizacionClient.objects.all().filter(state=1, client=client)
    return cotizacion_client


def getClient(client, obj):
    for cli in client:
        if cli.id == obj.client_id:
            return cli


def getCotizacion(cotizacion, obj):
    for coti in cotizacion:
        if coti.id == obj.cotizacion_id:
            return coti


def get_cloth(cotizacion):
    cloth_obj = Cloth.objects.all().filter(state=1)
    for cloth in cloth_obj:
        if cloth.id == cotizacion.cloth_id:
            return cloth


def getClothWithRental(cloth):
    return Alquiler.objects.all().filter(state=1, cloth_id=cloth.id)


def getClothWithCotizacion(cloth):
    return Cotizacion.objects.all().filter(state=1, cloth_id=cloth.id)


def getTotal(cotizaciones):
    if not cotizaciones:
        return 0
    else:
        cotizacion = cotizaciones[0]
        total1 = cotizacion.value_cloth + cotizacion.value_work
        total2 = cotizacion.value_threads + cotizacion.value_buttons
        total3 = cotizacion.value_necks + cotizacion.value_embroidery + cotizacion.value_prints
        total = total1 + total2 + total3
        return total


def FormClothInCotizacion():
    cloth = Cloth.objects.filter(state=1)
    cotizaciones = Cotizacion.objects.filter(state=1).values_list('cloth', flat=True)
    cloth_cotizacion = Cloth.objects.exclude(id__in=cotizaciones)
    return cloth_cotizacion


def ClothWithOutRental():
    cloth = Cloth.objects.filter(state=1)
    rentals = Alquiler.objects.filter(ifrental=1).values_list('cloth', flat=True)
    cloth_rental = Cloth.objects.exclude(id__in=rentals)
    return cloth_rental
