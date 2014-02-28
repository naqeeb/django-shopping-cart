from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=255)
    site = models.OneToOneField(Site)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = 'store'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    sku = models.CharField(max_length=255, null=True)
    store = models.ManyToManyField(Store, through='StoreProduct')

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = 'product'


class StoreProduct(models.Model):
    store = models.ForeignKey(Store)
    product = models.ForeignKey(Product)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'store_product'

class ProductAttribute(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = 'product_attribute'

class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product)
    attribute = models.ForeignKey(ProductAttribute)
    value = models.CharField(max_length=255)

    class Meta:
        db_table = 'product_attribute_value'

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

class Order(models.Model):
    store = models.ForeignKey(Store)
    user = models.ForeignKey(User)
    external_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        db_table = 'order'

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        db_table = 'order_item'

