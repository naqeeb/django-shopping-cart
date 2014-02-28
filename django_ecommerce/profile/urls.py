from django.conf.urls import patterns, include, url
import signals

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_shopping_cart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('registration.backends.default.urls')),
)
