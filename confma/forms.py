from django.forms import ModelForm , TextInput
from django import forms
from .models import User , Cotizacion

class UserFormModel(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'lastname',
            'address',
            'phone',
            'cellphone'
            
        ]
        widgets = {
            'name' : forms.TextInput( attrs = {'placeholder' : 'Your Name' , 'class' : 'form-control'}),
            'lastname' : forms.TextInput( attrs = {'placeholder' : 'Your LastName' , 'class' : 'form-control'}),
            'address' : forms.TextInput( attrs = {'placeholder' : 'Your Address' , 'class' : 'form-control'}),
            'phone' : forms.NumberInput( attrs = {'placeholder' : 'Your Phone' , 'class' : 'form-control'}),
            'cellphone' : forms.NumberInput( attrs = {'placeholder' : 'Your CellPhone' , 'class' : 'form-control'}),
        }

class UserForm(forms.Form):
    name = forms.CharField( max_length=100,
                            # help_text='Use puns liberally',
                            widget = forms.TextInput(
                                attrs = {
                                    "title" : "Name",
                                    "placeholder" : "Your Name",
                                    "class" : "form-control"
                                    }
                                )
                            )

    lastname = forms.CharField( max_length=100,
                                widget = forms.TextInput(
                                    attrs = {
                                        "placeholder" : "Your LastName",
                                        "class" : "form-control"
                                        }
                                    )
                                )

    address = forms.CharField( max_length=100,
                                required = False,
                                widget = forms.TextInput(
                                    attrs = {
                                        "placeholder" : "Your Address",
                                        "class" : "form-control"
                                        }
                                    )
                                )

    phone = forms.IntegerField(required = False,
                                widget = forms.NumberInput(
                                    attrs = {
                                        "placeholder" : "Your Phone",
                                        "class" : "form-control"
                                        }
                                    )
                                )

    cellphone = forms.IntegerField(widget = forms.NumberInput(
                                    attrs = {
                                        "placeholder" : "Your Cellphone",
                                        "class" : "form-control"
                                        }
                                    )
                                )


FASHION_CHOICE = [
    ('General' , 'general'),
    ('A medida' , 'a medida')
]

class CotizacionFormModel(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = [
            'value_cloth',
            'value_work',
            'value_threads',
            'value_buttons',
            'value_necks',
            'value_embroidery',
            'value_prints',
            'fashion',
            'subtotal',
            'total',
            
            ]
            
        widgets = {
            'name'              : forms.TextInput(attrs = {'placeholder' : 'Your Name' , 'class' : 'form-control'}),
            'lastname'          : forms.TextInput(attrs = {'placeholder' : 'Your LastName' , 'class' : 'form-control'}),
            'address'           : forms.TextInput(attrs = {'placeholder' : 'Your Address' , 'class' : 'form-control'}),
            'phone'             : forms.NumberInput(attrs = {'placeholder' : 'Your Phone' , 'class' : 'form-control'}),
            'cellphone'         : forms.NumberInput(attrs = {'placeholder' : 'Your CellPhone' , 'class' : 'form-control'}),
            'value_cloth'       : forms.NumberInput(attrs = {'placeholder' : 'Valor de la Tela' , 'class' : 'form-cotrol'}),
            'value_work'        : forms.NumberInput(attrs = {'placeholder' : 'Valor de la Tela' , 'class' : 'form-cotrol'}),
            'value_threads'     : forms.NumberInput(attrs = {'placeholder' : 'Valor de la Tela' , 'class' : 'form-cotrol'}),
            'value_buttons'     : forms.NumberInput(attrs = {'placeholder' : 'Valor de la Tela' , 'class' : 'form-cotrol'}),
            'value_necks'       : forms.NumberInput(attrs = {'placeholder' : 'Valor de la Tela' , 'class' : 'form-cotrol'}),
            'value_embroidery'  : forms.NumberInput(attrs = {'placeholder' : 'Valor de la Tela' , 'class' : 'form-cotrol'}),
            'value_prints'      : forms.NumberInput(attrs = {'placeholder' : 'Valor de la Tela' , 'class' : 'form-cotrol'}),
            'fashion'           : forms.Select(choices = FASHION_CHOICE),
            'subtotal'          : forms.NumberInput(attrs = {'placeholder' : 'Valor de la Tela' , 'class' : 'form-cotrol'}),
            'total'             : forms.NumberInput(attrs = {'placeholder' : 'Valor de la Tela' , 'class' : 'form-cotrol'})
        }