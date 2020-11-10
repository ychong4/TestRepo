from django.contrib import admin
from .models import Category, Pet

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Pet)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'adoption_fee', 'available',
                     'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['adoption_fee', 'available']
    prepopulated_fields = {'slug': ('name',)}