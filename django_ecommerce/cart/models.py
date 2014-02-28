from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from core.models import Store
from product.models import Product

class Cart(models.Model):
    store = models.ForeignKey(Store)
    user = models.ForeignKey(User, null=True, blank=True)
    session = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'cart'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'cart_item'
