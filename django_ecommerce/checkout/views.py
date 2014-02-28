from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.db.models import F
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

import random
from core.models import Store, Order, OrderItem
from cart.models import Cart, CartItem

@login_required
def checkout(request, template_name='checkout/complete.html'):
    response = {
        'store': None,
        'order': None,
        'order_items': None
    }

    # Get the current site
    site = get_current_site(request)

    # Get the current store
    store = Store.objects.get(site=site)

    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    # Create Order
    order_number = random.randint(100000, 900000)
    order = Order.objects.create(store=store, user=request.user, external_id=order_number, total=cart.total, status='New')
    response['order'] = order

    # Convert cart to order
    order_items = []
    for cart_item in cart_items:
        order_item = OrderItem.objects.create(order=order, quantity=cart_item.quantity, price=cart_item.product.price, product=cart_item.product)
        order_items.append(order_item)
        cart_item.delete()

    response['order_items'] = order_items
    cart.delete()

    return render_to_response(template_name, response, context_instance=RequestContext(request))
