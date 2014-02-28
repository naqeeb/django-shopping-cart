from django.contrib import admin
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from core.models import Store
from product.models import Product, StoreProduct, ProductAttribute, ProductAttributeValue
from profile.models import UserProfile, UserStoreProfile

from .utils import limit_qs_by_user, get_products_by_user


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'site')
    search_fields = ('name', 'site')

    def queryset(self, request):
        qs = super(StoreAdmin, self).queryset(request)
        return limit_qs_by_user(request.user, qs)

admin.site.register(Store, StoreAdmin)

class UserStoreProfileAdmin(admin.ModelAdmin):
    list_display = ('user_profile','store')

admin.site.register(UserStoreProfile, UserStoreProfileAdmin)


class StoreProductInline(admin.TabularInline):
    model = StoreProduct
    extra = 1

class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'sku')
    search_fields = ('name', 'description')
    inlines= [ProductAttributeValueInline, StoreProductInline]


admin.site.register(Product, ProductAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def queryset(self, request):
        qs = super(ProductAttributeAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.none()

admin.site.register(ProductAttribute, ProductAttributeAdmin)

class StoreProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'active')
    search_fields = ('product__name',)
    list_filter = ('store__name', 'active')

    def queryset(self, request):
        qs = super(StoreProductAdmin, self).queryset(request)
        return limit_qs_by_user(request.user, qs)

admin.site.register(StoreProduct, StoreProductAdmin)
