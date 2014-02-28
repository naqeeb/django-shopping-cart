from django.conf.urls import patterns, include, url
from product import views

urlpatterns = patterns('',
    url(r'^(?P<product_sku>[a-zA-Z0-9-]+)/$', views.product_detail, name='product_detail'),
)
