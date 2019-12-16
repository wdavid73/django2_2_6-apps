from django.shortcuts import render ,redirect , get_object_or_404
from django.http import Http404 , HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from ..forms.users import UserFormModel
from django.views.generic import (CreateView ,UpdateView , ListView ,DeleteView)

def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_api')
        else:
            return HttpResponse("NO INICIO DE SESION")

    context = {}
    return render(request , "loading.html" , context)

class UserCreateView(CreateView):
    template_name = "registration/login.html"
    form_class = UserFormModel
    queryset = User.objects.all()

    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../'