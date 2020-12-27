from decimal import Decimal
from django.conf import settings
from shop_app.models import Product

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
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # marca a seção como modificada e certifica que foi salva
        self.session.modified = True

    def remove(self, product):
        """
        Remove um produto do carrinho.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iteração sobre os items no carringo para receber os produtos da base de dados.
        """
        product_ids = self.cart.keys()
        # pega os objetos do produto e adiciona ao carrinho
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

        def __len__(self):
            """
            Conta todos os items no carrinho.
            """
            return sum(item['quantity'] for item in self.cart.values())

        def get_total_price(self):
            return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

        def clear(self):
            # remove o carrinho da seção
            del self.session[settings.CART_SESSION_ID]
            self.save()
