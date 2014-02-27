from django.conf.urls import patterns, include, url
from core import views

urlpatterns = patterns('',
	url(r'^product/(?P<product_sku>[a-zA-Z0-9-]+)/$', views.product_detail, name='product_detail'),

    url(r'^cart/add/$', views.add_product_to_cart, name='add_product_to_cart'),

    url(r'', views.home, name='home'),
)
