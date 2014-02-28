from django.contrib.auth import login
from django.contrib.sites.models import get_current_site
from django.dispatch import receiver
from django.shortcuts import redirect

from registration.signals import user_activated
from core.models import Store
from profile.models import UserProfile, UserStoreProfile

@receiver(user_activated)
def login_on_activation(sender, user, request, **kwargs):
    print 'Signal Received'
    """Creates User Profile"""
    # Get the current site
    site = get_current_site(request)

    # Get the current store
    store = Store.objects.get(site=site)

    user_profile, up_created = UserProfile.objects.get_or_create(user=user)
    user_store_profile, usp_created = UserStoreProfile.objects.get_or_create(user=user_profile, store=store)

    """Logs in the user after activation"""
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
