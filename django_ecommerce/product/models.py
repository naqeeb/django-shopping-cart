from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    sku = models.CharField(max_length=255, null=True)
    store = models.ManyToManyField('core.Store', through='StoreProduct')

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = 'product'


class StoreProduct(models.Model):
    store = models.ForeignKey('core.Store')
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
