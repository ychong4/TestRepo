from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import EmployeeAdmin


# Register your models here.
class EmployeeUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = EmployeeAdmin
    list_display = ['username', 'role', 'is_staff']


admin.site.register(EmployeeAdmin, EmployeeUserAdmin)