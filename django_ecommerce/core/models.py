from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = 'store'

class Order(models.Model):
    store = models.ForeignKey(Store)
    user = models.ForeignKey(User)
    external_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=9, decimal_places=2)

    def __unicode__(self):
        return u'%s|%s' % (self.store.name, self.external_id)

    class Meta:
        db_table = 'orders'

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey('product.Product')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        db_table = 'order_item'

