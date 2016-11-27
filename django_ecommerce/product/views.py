from django.db.models import F
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

from cart.forms import AddProductToCartForm
from cart.models import Cart, CartItem

from core.models import Store

from product.models import Product, StoreProduct, ProductAttributeValue

def product_detail(request, product_sku, template_name='product/product.html'):
    pass
    # Get the current site
    response = {
        'store': None,
        'product': None,
        'product_attributes': None,
        'add_to_cart_form': None,
    }

    # Get the current store
    store = Store.objects.filter(site=site)
    response['store'] = store

    # Get the store and the product based on the sku
    store_products = StoreProduct.objects.filter(store=store, active=True).filter(product__sku=product_sku)

    # Redirect to homepage if product is not found
    if not store_products:
        return redirect('home')

    store_product = store_products[0]
    product = store_product.product
    product_attributes = ProductAttributeValue.objects.filter(product=product)
    response['product'] = product
    response['product_attributes'] = product_attributes

    response['add_to_cart_form'] = AddProductToCartForm(initial={'sku': store_product.product.sku })

    return render_to_response(template_name, response, context_instance=RequestContext(request))
