from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    def __init__(self, request):
        """
        Inicializa o carrinho.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # salva um carrinho cazio na sessão
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    def add(self, product, quantity=1, override_quantity=False):
        """
        Adiciona um produto ao carrinho e atualiza a quantidade.
        """
        product_id = str(product.id)
        if product_id not in self.Cart:
            self.cart[roduct_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id] = ['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True 
