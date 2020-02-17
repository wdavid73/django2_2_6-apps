from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Insert Your First Name", required=False)
    last_name = forms.CharField(label="Insert Your Last Name", required=False)
    email = forms.CharField(label="Insert a e-mail", required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
