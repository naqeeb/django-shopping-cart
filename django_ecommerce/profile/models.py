from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    site = models.ManyToManyField(Site, through='UserSiteProfile')

class UserSiteProfile(models.Model):
    user =  models.ForeignKey(UserProfile)
    site = models.ForeignKey(Site)