from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from ..forms.signup import SignUpForm

"""metodo que usa el CREATEVIEW de django para hacer la vista 
donde se van a registrar los usuarios"""
class SignUp(generic.CreateView):
    # form_class = UserCreationForm
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

