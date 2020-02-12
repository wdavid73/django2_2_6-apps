from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Models
from ..models import Cloth, Alquiler, Client
# Form
from ..forms.cloth import ClothFormModel
from ..forms.rental import RentalForm
# Create your views here.
from django.views.generic import (CreateView, UpdateView, ListView, DeleteView)


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


class CreateRental(CreateView):
    template_name = "rental/create.html"
    form_class = RentalForm

    def form_valid(self, form):
        now = date.today()
        if form.cleaned_data["date_return"] > now:
            if form.cleaned_data["client"].state == 1:
                return super().form_valid(form)
            else:
                return redirect('confma:create_rental')
        else:
            return redirect('confma:create_rental')

    def get_success_url(self):
        return '../../../../'


class ListOfAllRental(ListView):
    template_name = 'rental/details.html'
    if not Client.DoesNotExist:
        list_client = list(Client.objects.all().filter(state=1))
        queryset = Alquiler.objects.filter(state=1).filter(client__in=list_client)
    else:
        queryset = Alquiler.objects.filter(state=1)


def HomePage(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, "index.html", {})
    else:
        return render(request, "home.html", {})


def handler404(request, *args, **argv):
    response = render_to_response(
        '404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
