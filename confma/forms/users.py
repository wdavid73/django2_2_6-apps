from django.forms import ModelForm , TextInput
from django import forms
from django.contrib.auth.models import User

class UserFormModel(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            
        ]
        widgets = {
            'username' : forms.TextInput( attrs = {'placeholder' : 'Your UserName' , 'class' : 'form-control'}),
            'password' : forms.PasswordInput( attrs = {'placeholder' : 'Your Password' , 'class' : 'form-control'}),
        }