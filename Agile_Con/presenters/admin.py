from django.contrib import admin
from .models import Presenter


# Register your models here.
class PresenterAdmin(admin.ModelAdmin):
    model = Presenter


admin.site.register(Presenter, PresenterAdmin)
