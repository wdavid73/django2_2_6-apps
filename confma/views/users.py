from django.shortcuts import render ,redirect , get_object_or_404
from django.http import Http404 , HttpResponse
from django.urls import reverse

# Models
from ..models import User

#Forms
from ..forms.user import UserFormModel , UserForm

# Create your views here.
from django.views.generic import (CreateView ,UpdateView , ListView ,DeleteView)

def home(request , *args, **kwargs):
    obj = User.objects.all()
    context = {
        "user" : obj,
        "model" : "Users"
     }
    return render(request , "users/home_users.html" , context)

class UserCreateView(CreateView):
    template_name = "users/create.html"
    form_class = UserFormModel
    queryset = User.objects.all()

    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../'

def details(request):
    obj = User.objects.all()
    context = {
        "user" : obj
    }
    return render(request , "users/details.html" , context)

class UserListView(ListView):
    template_name = 'users/details.html'
    queryset = User.objects.all()



class UserDeleteView(DeleteView):
    template_name = 'users/delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User , id=id_)

    def get_success_url(self):
        return reverse('users:users_home')


class UserUpdateView(UpdateView):
    template_name = "users/update.html"
    form_class = UserFormModel

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User , id=id_)

    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '../../'

def deletelog(request , id):
    obj = get_object_or_404 (User , id=id)

    if request.method == 'POST':
        obj.state = 0
        obj.save()
        return redirect('../../')

    context = {
        'user' : obj
    }
    return render(request , 'users/deletel.html', context)


def restoreview(request):
    obj = User.objects.all()
    context = {
        'users' : obj
    }
    return render(request , 'users/restore.html', context)

def restore(request, id):
    obj = get_object_or_404(User , id=id)
    if request.method == 'POST':
        obj.state = 1
        obj.save()
        return redirect('../../')
        
    response = 'I Dont Know <a href = "/confma/users/"> BACK </a>'
    return HttpResponse(response)
    
