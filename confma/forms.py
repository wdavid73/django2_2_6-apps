from django.forms import ModelForm , TextInput
from django import forms
from .models import User

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

