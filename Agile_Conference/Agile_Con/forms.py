from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser, CustomerOrder, Attendee


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('attendee_id', 'username', 'email', 'first_name', 'last_name' , 'cell_phone')

    def save(self, commit=True):
        attendee_id = self.cleaned_data.get('attendee_id')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        cell_phone = self.cleaned_data.get('cell_phone')
        password1 = self.cleaned_data.get('password1')
        Attendee.objects.create(attendee_id=attendee_id, username=username, email=email, first_name=first_name, last_name=last_name, cell_phone=cell_phone)
        CustomUser.objects.create_user(attendee_id=attendee_id, username=username, email=email, first_name=first_name,
                                       last_name=last_name, cell_phone=cell_phone, password=password1)
        return Attendee


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('attendee_id', 'username', 'email', 'first_name', 'last_name' , 'cell_phone')

class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ('attendee', 'presentation')