from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=255)
    site = models.OneToOneField(Site)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    store = models.ManyToManyField(Store, through='StoreProduct')

class StoreProduct(models.Model):
    store = models.ForeignKey(Store)
    product = models.ForeignKey(Product)
    active = models.BooleanField(default=True)

class ProductAttribute(models.Model):
    name = models.CharField(max_length=255)

class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product)
    attribute = models.ForeignKey(ProductAttribute)
    value = models.CharField(max_length=255)

class Cart(models.Model):
    store = models.ForeignKey(Store)
    user = models.ForeignKey(User)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

class Order(models.Model):
    store = models.ForeignKey(Store)
    user = models.ForeignKey(User)
    status = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)