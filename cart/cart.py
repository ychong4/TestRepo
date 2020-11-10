from decimal import Decimal
from django.conf import settings
from pets.models import Pet

class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, pet, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        pet_id = str(pet.id)
        if pet_id not in self.cart:
            self.cart[pet_id] = {'quantity': 0,
                                     'price': str(pet.adoption_fee)}
        if override_quantity:
            self.cart[pet_id]['quantity'] = quantity
        else:
            self.cart[pet_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, pet):
        """
        Remove a product from the cart.
        """
        pet_id = str(pet.id)
        if pet_id in self.cart:
            del self.cart[pet_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        pet_ids = self.cart.keys()
        # get the product objects and add them to the cart
        pets = Pet.objects.filter(id__in=pet_ids)
        cart = self.cart.copy()
        for pet in pets:
            cart[str(pet.id)]['pet'] = pet
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()