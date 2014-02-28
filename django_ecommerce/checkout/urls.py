from django.conf.urls import patterns, include, url
from checkout import views

urlpatterns = patterns('',
    url(r'^complete/$', views.checkout, name='checkout'),
)
