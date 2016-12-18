from profile.models import UserStoreProfile, UserProfile
from product.models import Product

def get_stores_by_user(user):
    stores = None
    user_profile = user.get_profile()
    if user_profile:
        store_user_profiles = UserStoreProfile.objects.filter(user_profile=user_profile)
        stores = [store_user_profile.store for store_user_profile in store_user_profiles]

    return stores

def limit_qs_by_user(user, qs):
    if user.is_superuser:
        return qs

    stores = get_stores_by_user(user)
    if stores:
        return qs.filter(store__in=stores)

    return qs.none()

def get_products_by_user(user, qs):
    if user.is_superuser:
        return qs

    stores = get_stores_by_user(user)
    if stores:
        store_products = Product.objects.filter(store=store)
        products = [store_product.product for store_product in store_products]
        return products

    return qs.none()
