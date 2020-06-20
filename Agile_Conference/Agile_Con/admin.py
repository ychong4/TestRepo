from django.contrib import admin
from .models import  CustomUser, Presenter, Attendee, Presentation, CustomerOrder
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'cell_phone']

class AttendeeList(admin.ModelAdmin):
    list_display = ( 'attendee_id', 'username', 'email', 'cell_phone', 'first_name', 'last_name')
    list_filter = ( 'attendee_id', 'username', 'email', 'cell_phone', 'first_name', 'last_name')
    search_fields = ( 'attendee_id', 'username', 'email', 'cell_phone', 'first_name', 'last_name')
    ordering = ['attendee_id']

class PresenterList(admin.ModelAdmin):
    list_display = ( 'presenter_id', 'name', 'user' )
    list_filter = ( 'presenter_id', 'name', 'user' )
    search_fields = ( 'presenter_id', 'name', 'user' )
    ordering = ['presenter_id']

class PresentationList(admin.ModelAdmin):
    list_display = ( 'presenter_id', 'timeslot', 'cost' )
    list_filter = ( 'presenter_id', 'timeslot', 'cost' )
    search_fields = ( 'presenter_id', 'timeslot', 'cost' )
    ordering = ['presenter_id']

class CustomerOrderAdmin(admin.ModelAdmin):
    model = CustomerOrder

admin.site.register(CustomerOrder, CustomerOrderAdmin)
admin.site.register(Presenter)
admin.site.register(CustomUser)
admin.site.register(Attendee, AttendeeList)
admin.site.register(Presentation)