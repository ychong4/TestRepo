from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import EmployeeAdmin


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = EmployeeAdmin
        fields = ('username', 'role')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = EmployeeAdmin
        fields = ('username', 'role')