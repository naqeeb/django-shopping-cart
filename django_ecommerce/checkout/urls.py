from django.conf.urls import include, url
from checkout import views

urlpatterns = [
    url(r'^complete/$', views.checkout, name='checkout'),
]
