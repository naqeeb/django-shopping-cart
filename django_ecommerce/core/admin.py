from django.contrib import admin

from django.contrib.sites.models import Site
from core.models import Store
from product.models import Product, StoreProduct, ProductAttribute, ProductAttributeValue

from django.utils.translation import ugettext_lazy as _

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'site')
    search_fields = ('name', 'site')

admin.site.register(Store, StoreAdmin)

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

admin.site.register(ProductAttribute, ProductAttributeAdmin)

class StoreProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'active')
    search_fields = ('product__name',)
    list_filter = ('store__name', 'active')

admin.site.register(StoreProduct, StoreProductAdmin)
