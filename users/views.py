from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required()
def user_profile(request):
    user = request.user
    return render(request, "registration/user_profile.html", {'user':user})