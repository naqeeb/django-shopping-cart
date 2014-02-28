from django.contrib.sites.models import get_current_site
from django.db.models import F
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

from .models import Store, Product, StoreProduct, Cart, CartItem
from .forms import AddProductToCartForm

def product_detail(request, product_sku, template_name='core/product.html'):
    pass
    # Get the current site
    response = {
        'store': None,
        'product': None,
        'add_to_cart_form': None,
    }

    # Get the current site
    site = get_current_site(request)

    # Get the current store
    store = Store.objects.filter(site=site)
    response['store'] = store

    # Get the store and the product based on the sku
    store_products = StoreProduct.objects.filter(store=store, active=True).filter(product__sku=product_sku)

    # Redirect to homepage if product is not found
    if not store_products:
        return redirect('home')

    store_product = store_products[0]
    response['product'] = store_product.product

    response['add_to_cart_form'] = AddProductToCartForm(initial={'sku': store_product.product.sku })

    return render_to_response(template_name, response, context_instance=RequestContext(request))


def view_cart(request, cart_id, template_name='core/cart.html'):
    response = {
        'store': None,
        'cart': None,
        'cart_items': None
    }

    # Get the current site
    site = get_current_site(request)

    # Get the current store
    store = Store.objects.get(site=site)

    response['store'] = store
    cart = Cart.objects.get(pk=cart_id)
    response['cart'] = cart
    response['cart_items'] = CartItem.objects.filter(cart=cart)

    return render_to_response(template_name, response, context_instance=RequestContext(request))

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
            cart_item = CartItem(cart=cart, product=product, quantity=quantity)
            cart_item.save()
        else:
            # Increment the Item
            cart_item.quantity = F('quantity') + quantity
            cart_item.save()

        return redirect('view_cart', cart_id=cart.pk)

    return redirect('home')


def prepare_checkout(request, template_name='core/checkout.html'):
    pass
    # Find the cart

    # Check out only for logged in users


def checkout(request, template_name='core/checkout.html'):
    pass
    # Convert cart to order


def home(request, template_name='core/store.html'):
    response = {
        'store': None,
        'products': None
    }

    # Anonymous User Tracking
    if not request.user.is_authenticated():
        if not request.session.exists(request.session.session_key):
            request.session.create()

    # Get the current site
    site = get_current_site(request)

    # Get the current store
    store = Store.objects.filter(site=site)
    response['store'] = store

    store_products = StoreProduct.objects.filter(store=store, active=True)
    products = [store.product for store in store_products]
    response['products'] = products

    return render_to_response(template_name, response, context_instance=RequestContext(request))


