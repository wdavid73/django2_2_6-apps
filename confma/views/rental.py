from datetime import date

from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from confma.forms.rental import RentalForm
from confma.models import Alquiler, Client
from confma.static_methods import RentedClothes, FindClothByNameRental


# def CreateRental2(request):
#     if request.path == '/confma/api/v1/cloth/find/':
#         cloths = FindClothByNameRental(request)
#         display = True if cloths.count() > 0 else False
#         form = RentalForm
#         context = {
#             'cloths': cloths,
#             'display': display,
#             'cloth_name': request.GET.get('cloth_name'),
#             'form': form,
#         }
#         return render(request, 'rental/create.html', context)
#     elif request.path == '/confma/api/v1/rental/create2/':
#         if request.method == 'POST':
#             form = RentalForm(request.POST)
#             if form.is_valid():
#                 now = date.today()
#                 if form.cleaned_data['price'] > 0 and form.cleaned_data['date_return'] > now:
#                     if not RentedClothes(form):
#                         Alquiler.objects.create(**form.cleaned_data)
#                         return redirect('confma:list_of_all_rental')
#                 return redirect('confma:create2_rental')
#             return redirect('confma:create2_rental')
#         return redirect('confma:create2_rental')


class CreateRental(CreateView):
    template_name = "rental/create.html"
    form_class = RentalForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['cloth'] = ClothWithOutRental()
    #     return context

    def form_valid(self, form):
        now = date.today()
        if form.cleaned_data["date_return"] > now:
            if form.cleaned_data["client"].state == 1:
                if RentedClothes(form):
                    return redirect('confma:create_rental')
                return super().form_valid(form)
            return redirect('confma:create_rental')
        return redirect('confma:create_rental')

    def get_success_url(self):
        return reverse('confma:list_of_all_rental')


class ListOfAllRental(ListView):
    template_name = 'rental/details.html'
    if not Client.DoesNotExist:
        list_client = list(Client.objects.all().filter(state=1))
        queryset = Alquiler.objects.filter(state=1, ifrental=1).filter(client__in=list_client)
    else:
        queryset = Alquiler.objects.filter(state=1, ifrental=1)


def RefundRental(request, _id):
    rental = get_object_or_404(Alquiler, id=_id)
    if request.method == 'POST':
        rental.ifrental = 0
        rental.save()
        return redirect('confma:list_of_all_rental')


def FindClothRental(request):
    cloths = FindClothByNameRental(request)
    display = True if cloths.count() > 0 else False
    context = {
        'cloths': cloths,
        'display': display,
        'cloth_name': request.GET.get('cloth_name'),
        'form': RentalForm,
    }
    return render(request, 'rental/create.html', context)
