from django.shortcuts import render_to_response, render

from confma.models import Cloth, Alquiler, Cotizacion


def ClothWithOutRental():
    rentals = Alquiler.objects.filter(ifrental=1).values_list('cloth', flat=True)
    cloth_rental = Cloth.objects.exclude(id__in=rentals)
    return cloth_rental


def ClothWithOutCotizacion():
    cotizaciones = Cotizacion.objects.filter(state=1).values_list('cloth', flat=True)
    cloth_cotizacion = Cloth.objects.exclude(id__in=cotizaciones)
    return cloth_cotizacion


def RentedClothes(form):
    cloth = Cloth.objects.filter(id=form.cleaned_data['cloth'].id)
    if Alquiler.objects.filter(cloth__in=list(cloth), ifrental=1):
        return True
    return False


def getCotizacionWithCloth(Cotizacion, Cloth):
    cloth = list(Cloth.objects.all())
    queryset = Cotizacion.objects.all().filter(state=1, cloth__in=cloth)
    return queryset


def ClothDuplicated(form):
    cloth = Cloth.objects.filter(id=form.cleaned_data['cloth'].id)
    if Cotizacion.objects.filter(cloth__in=list(cloth)):
        return True


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
    if cotizaciones:
        total1 = cotizaciones.value_cloth + cotizaciones.value_work
        total2 = cotizaciones.value_threads + cotizaciones.value_buttons
        total3 = cotizaciones.value_necks + cotizaciones.value_embroidery + cotizaciones.value_prints
        total = total1 + total2 + total3
        return total
    else:
        return 0


def FindClothByNameRental(request):
    _name = request.GET.get('cloth_name')
    cloth = Cloth.objects.filter(name=_name, id__in=list(ClothWithOutRental().values_list('id', flat=True)))
    return cloth


def FindClothByNameCotizacion(request):
    _name = request.GET.get('cloth_name')
    cloth = Cloth.objects.filter(name=_name, id__in=list(ClothWithOutCotizacion().values_list('id', flat=True)))
    return cloth


def ClothIfRental(Cloth, Alquiler):
    cloth = Cloth.objects.all().filter(state=1)
    for clo in cloth:
        rental = Alquiler.objects.all().get(cloth_id=clo.id)
        print(rental)
