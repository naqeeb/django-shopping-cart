from django.conf.urls import include, url
import signals

urlpatterns = [
    url(r'', include('registration.backends.hmac.urls')),
]
