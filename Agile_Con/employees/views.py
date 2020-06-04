from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create your views here.

class SignUpView(generic.CreateView):
   form_class = CustomUserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'signup.html'


def home(request):
   return render(request, 'home.html')



