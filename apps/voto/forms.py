from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import usuario,pregunta

class Userform(UserCreationForm):
	mail = forms.CharField(max_length=64)
	name = forms.CharField(max_length=64)
	last = forms.CharField(max_length=64)