from django.forms import ModelForm , TextInput
from django import forms

from ..models import Cotizacion , Client , Cotizacion_Client

class CUFormModel(forms.ModelForm):
    class Meta:
        model = Cotizacion_Client
        fields = [
            'cotizacion',
            'client',
            'total'
            ]
            
        widgets = {
            'cotizacion'       	: forms.SelectMultiple(attrs = {'class' : 'form-control'}),
            'client'        		: forms.SelectMultiple(attrs = {'class' : 'form-control'}),
        }

class Coti_UserFormModel(forms.ModelForm):
    class Meta:
        model = Cotizacion_Client
        exclude = ["state"]
        def __init__ (self , *args , **kwargs):
            # brand = kwargs.pop("brand")
            super(Coti_UserFormModel , self).__init__(*args , **kwargs)
            self.fields["cotizacion"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["cotizacion"].help_text = ""
            self.fields["cotizacion"].queryset = Cotizacion.object.all()
            self.fields["client"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["client"].help_text = ""
            self.fields["client"].queryset = User.object.all()


