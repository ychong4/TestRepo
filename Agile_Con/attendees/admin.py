from django.contrib import admin
from .models import Attendee


# Register your models here.
class AttendeeAdmin(admin.ModelAdmin):
    model = Attendee


admin.site.register(Attendee, AttendeeAdmin)
