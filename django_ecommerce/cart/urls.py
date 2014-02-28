from django.conf.urls import patterns, include, url
from cart import views

urlpatterns = patterns('',
    url(r'^add/$', views.add_product_to_cart, name='add_product_to_cart'),
    url(r'^(?P<cart_id>[0-9]+)/$', views.view_cart, name='view_cart'),
)
