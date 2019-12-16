from django.shortcuts import render ,redirect , get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404 , HttpResponse
from datetime import date

# Models
from ..models import Cloth , Alquiler , Client
#Form
from ..forms.cloth import ClothFormModel 
from ..forms.alquiler import AlquilerFormModel
# Create your views here.
from django.views.generic import (CreateView ,UpdateView , ListView ,DeleteView)

class ClothCreateView(CreateView):
    template_name = "cloth/create.html"
    form_class = ClothFormModel
    queryset = Cloth.objects.all()

    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../../'

class AlquilerCreateView(CreateView):
    template_name = "alquiler/create.html"
    form_class = AlquilerFormModel
    queryset = Alquiler.objects.all()

    def form_valid(self , form):
        print(form.cleaned_data)
        now = date.today()        
        if form.cleaned_data["date_return"] > now:
            return super().form_valid(form)
        else:
            return HttpResponse("NO CUMPLE LA FECHA")

    def get_success_url(self):
        return '../../'

class AlquilerListView(ListView):
     template_name = 'alquiler/details.html'
     queryset = Alquiler.objects.all()

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cloth_list'] = Cloth.objects.all()
        context['client_list'] = Client.objects.all()
        return context


def home_view(request , *args, **kwargs):
    return render(request , "home.html" , {})

def home_api(request , *args, **kwargs):
    return render(request , "index.html" , {})


def handler404(request, *args, **argv):
    response = render_to_response(
    			'404.html', {},
                context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response