from django.conf.urls import include, url
from rest_framework import routers

from django.contrib import admin
admin.autodiscover()

from core import views, viewsets

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'orders', viewsets.OrderViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('profile.urls')),
    url(r'^product/', include('product.urls')),
    url(r'^carts/', include('cart.urls')),
    url(r'^checkout/', include('checkout.urls')),
    url(r'^home/', views.home, name='home'),
]

urlpatterns += router.urls
