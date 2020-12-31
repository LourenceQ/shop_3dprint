from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if dorm.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order= order, product=item['product'], price=item['price'],quantity_item['quantity'])
            # limpa o carrinho
            cart.clear()
            return render(request,'orders_app/order/created.html',{'order': order})
        else:
            form = OrderCreateForm()
        return render(request,'orders_app/order/create.html',{'cart': cart, 'form': form}
