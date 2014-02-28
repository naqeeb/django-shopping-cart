from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

from localflavor.us.models import USStateField

from core import constants

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    store = models.ManyToManyField('core.Store', through='UserStoreProfile')

    def __unicode__(self):
        return u'%s' % (self.user.email)

    class Meta:
        db_table = 'user_profile'


class UserStoreProfile(models.Model):
    user_profile =  models.ForeignKey(UserProfile)
    store = models.ForeignKey('core.Store')

    class Meta:
        db_table = 'user_store_profile'

class UserAddress(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = USStateField()
    zip_code = models.CharField(max_length=5)
    type = models.CharField(max_length=100, choices=[(x,x) for x in constants.USER_ADDRESS_TYPES])

    class Meta:
        db_table = 'user_address'
