from django.db.models import F
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext

from cart.forms import AddProductToCartForm
from cart.models import Cart, CartItem

from core.models import Store

from product.models import Product, ProductAttributeValue

def product_detail(request, product_sku, template_name='product/product.html'):
    # Get the current site
    response = {
        'store': None,
        'product': None,
        'product_attributes': None,
        'add_to_cart_form': None,
    }

    # Get the current store
    store = Store.objects.filter(id=1)
    response['store'] = store

    # Get the store and the product based on the sku
    products = Product.objects.filter(store=store, active=True).filter(sku=product_sku)

    # Redirect to homepage if product is not found
    if not products:
        return redirect('home')

    product = products[0]
    product_attributes = ProductAttributeValue.objects.filter(product=product)
    response['product'] = product
    response['product_attributes'] = product_attributes

    response['add_to_cart_form'] = AddProductToCartForm(initial={'sku': product.sku })

    return render(request, template_name, context=response)
