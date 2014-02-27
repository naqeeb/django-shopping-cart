from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from .models import Store, Product, StoreProduct
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


def add_product_to_cart(request, template_name='core/cart.html'):
    response = {
        'store': None,
        'cart': None
    }

    # Get the current site
    site = get_current_site(request)

    # Get the current store
    store = Store.objects.filter(site=site)

    form = AddProductToCartForm(request.POST or None)

    if form.is_valid():
        # Use the user or session to find the cart
        user_authenticated = request.user.is_authenticated()
        sku = form.cleaned_data['sku']
        quantity = form.cleaned_data['quantity']

        # Get the cart
        cart = None
        product = None
        if user_authenticated:
            try:
                cart = Cart.objects.get(user=request.user)
                cart_items = CartItems.objects.filter(cart=cart)
                products = [cart_item.product for cart_item in cart_items if cart_item.product__sku == sku]
                if products:
                    product = products[0]
            except:
                cart = Cart.objects.create(store=store, user=request.user)
        else:
            session_key = request.session.session_key
            try:
                cart = Cart.objects.get(session=session_key)
                cart_items = CartItems.objects.filter(cart=cart)
                products = [cart_item.product for cart_item in cart_items if cart_item.product__sku == sku]
                if products:
                    product = products[0]
            except:
                cart = Cart.objects.create(store=store,session=session_key)

        #
        if not product:
            # Create Cart Item
            pass
        else:
            # Increment the Item
            pass


        # Check the cart items to see if the product was add to the cart previously

        # Add or increment the item


    return render_to_response(template_name, response, context_instance=RequestContext(request))


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


