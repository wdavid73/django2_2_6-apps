from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.CharField()

	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)