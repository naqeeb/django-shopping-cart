from django.db.models import F
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext

from .models import Store
from product.models import Product

def home(request, template_name='core/store.html'):
    response = {
        'store': None,
        'products': None
    }

    # Anonymous User Tracking
    if not request.user.is_authenticated():
        if not request.session.exists(request.session.session_key):
            request.session.create()

    # Get the current store
    store = Store.objects.filter(id=1)
    response['store'] = store

    products = Product.objects.filter(store=store, active=True)
    response['products'] = products

    return render(request,template_name, context=response)


