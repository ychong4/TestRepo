from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from pets.models import Pet
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required

@require_POST
def cart_add(request, pet_id):
    cart = Cart(request)
    pet = get_object_or_404(Pet, id=pet_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(pet=pet,

                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, pet_id):
    cart = Cart(request)
    pet = get_object_or_404(Pet, id=pet_id)
    cart.remove(pet)
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})