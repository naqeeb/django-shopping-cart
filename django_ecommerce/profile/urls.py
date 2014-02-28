from django.conf.urls import patterns, include, url
import signals

urlpatterns = patterns('',
    url(r'', include('registration.backends.default.urls')),
)
