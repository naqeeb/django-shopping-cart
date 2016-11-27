from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from core import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('profile.urls')),
    url(r'^product/', include('product.urls')),
    url(r'^carts/', include('cart.urls')),
    url(r'^checkout/', include('checkout.urls')),
    url(r'', views.home, name='home'),
]
