from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Category, Pet
from cart.forms import CartAddProductForm
import braintree
from pethome import settings
from django.http import HttpResponse



def pet_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    pets = Pet.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        pets = pets.filter(category=category)
    return render(request,
                  'pethome/list.html',
                  {'category': category,
                   'categories': categories,
                   'pets': pets})

def pet_detail(request, id, slug):
    pet = get_object_or_404(Pet,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'pethome/detail.html',
                  {'pet': pet,
                   'cart_product_form': cart_product_form})

def home(request):
   return render(request, 'pets/pethome/home.html',
                 {'pethome': home})

def about_us(request):
    return render(request, 'pethome/about_us.html',
                  {'about_us': about_us})

def donate(request):
    return render(request, 'pethome/donate.html')


