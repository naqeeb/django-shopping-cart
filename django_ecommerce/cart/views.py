from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

from core.models import Store
from product.models import Product, StoreProduct
from .models import Cart, CartItem
from .forms import AddProductToCartForm


@login_required
def view_cart(request, cart_id, template_name='cart/cart.html'):
    response = {
        'store': None,
        'cart': None,
        'cart_items': None
    }

    # Get the current site
    store = Store.objects.get(id=1)

    response['store'] = store
    cart = Cart.objects.get(pk=cart_id)
    cart_items = CartItem.objects.filter(cart=cart)

    response['cart'] = cart
    response['cart_items'] = cart_items

    return render_to_response(template_name, response, context_instance=RequestContext(request))

@login_required
def add_product_to_cart(request):
    cart = None

    # Get the current site
    site = get_current_site(request)

    # Get the current store
    store = Store.objects.get(site=site)

    form = AddProductToCartForm(request.POST or None)

    if form.is_valid():
        # Use the user or session to find the cart
        user_authenticated = request.user.is_authenticated()
        sku = form.cleaned_data['sku']
        quantity = long(form.cleaned_data['quantity'])
        product = get_object_or_404(Product, sku=sku)

        # Get the cart
        cart_item = None
        if user_authenticated:
            try:
                cart = Cart.objects.get(user=request.user)
                cart_items = CartItem.objects.filter(cart=cart)

                for item in cart_items:
                    if item.product.sku == sku:
                        cart_item = item
                        break
            except Cart.DoesNotExist:
                cart = Cart.objects.create(store=store, user=request.user)
            except Exception as e:
                print e

        else:
            session_key = request.session.session_key
            try:
                cart = Cart.objects.get(session=session_key)
                cart_items = CartItem.objects.filter(cart=cart)

                for item in cart_items:
                    if item.product.sku == sku:
                        cart_item = item
                        break
            except Cart.DoesNotExist:
                cart = Cart.objects.create(store=store, session=session_key)
            except Exception as e:
                print e

        # Check the cart items to see if the product was added previously
        if not cart_item:
            # Create Cart Item
            total = product.price * Decimal(quantity)

            cart_item = CartItem(cart=cart, product=product, quantity=quantity, total=total)
            cart_item.save()
        else:
            # Increment the Item
            new_quantity = cart_item.quantity + quantity
            cart_item.total = product.price * Decimal(new_quantity)
            cart_item.quantity = new_quantity
            cart_item.save()

        # Recalculate the cart total
        cart_items = CartItem.objects.filter(cart=cart)
        new_cart_total = Decimal('0.0')

        for item in cart_items:
            new_cart_total = new_cart_total + item.total

        if new_cart_total:
            cart.total = new_cart_total
            cart.save()

        return redirect('view_cart', cart_id=cart.pk)

    return redirect('home')
