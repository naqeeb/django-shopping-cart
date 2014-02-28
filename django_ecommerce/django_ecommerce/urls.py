from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from core import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('profile.urls')),
    url(r'^product/', include('product.urls')),
    url(r'^carts/', include('cart.urls')),
    url(r'', views.home, name='home'),
)
