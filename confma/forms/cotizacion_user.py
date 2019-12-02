from django.forms import ModelForm , TextInput
from django import forms

from ..models import Cotizacion , User , Cotizacion_User

class CUFormModel(forms.ModelForm):
    class Meta:
        model = Cotizacion_User
        fields = [
            'cotizacion',
            'user',
            'total'
            ]
            
        widgets = {
            'cotizacion'       	: forms.SelectMultiple(attrs = {'class' : 'form-control'}),
            'user'        		: forms.SelectMultiple(attrs = {'class' : 'form-control'}),
        }

class Coti_UserFormModel(forms.ModelForm):
    class Meta:
        model = Cotizacion_User
        exclude = ["state"]
        def __init__ (self , *args , **kwargs):
            # brand = kwargs.pop("brand")
            super(Coti_UserFormModel , self).__init__(*args , **kwargs)
            self.fields["cotizacion"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["cotizacion"].help_text = ""
            self.fields["cotizacion"].queryset = Cotizacion.object.all()
            self.fields["user"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["user"].help_text = ""
            self.fields["user"].queryset = User.object.all()


