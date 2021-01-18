from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from . forms import registerForm

class register(generic.CreateView):
	form_class = registerForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')