from django.contrib.sites.models import get_current_site
from django.db.models import F
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

from .models import Store, Product, StoreProduct, Cart, CartItem
from .forms import AddProductToCartForm

def prepare_checkout(request, template_name='core/checkout.html'):
    pass
    # Find the cart

    # Check out only for logged in users


def checkout(request, template_name='core/checkout.html'):
    pass
    # Convert cart to order
