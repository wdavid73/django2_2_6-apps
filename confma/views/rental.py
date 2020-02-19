from datetime import date

from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView

from confma.forms.rental import RentalForm
from confma.models import Alquiler, Cloth, Client


def RentedClothes(form):
    cloth = Cloth.objects.filter(id=form.cleaned_data['cloth'].id)
    if Alquiler.objects.filter(cloth__in=list(cloth), ifrental=1):
        return True


class CreateRental(CreateView):
    template_name = "rental/create.html"
    form_class = RentalForm

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
