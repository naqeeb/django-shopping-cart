from django.conf.urls import include, url
from product import views

urlpatterns = [
    url(r'^(?P<product_sku>[a-zA-Z0-9-]+)/$', views.product_detail, name='product_detail'),
]
