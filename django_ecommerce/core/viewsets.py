from rest_framework import viewsets

from core.rest.viewsets import BaseViewSet

from .models import Order
from .serializers import OrderListSerializer

class OrderViewSet(BaseViewSet, viewsets.ReadOnlyModelViewSet):
    serializers = {
        'list':    OrderListSerializer,
        'default':  OrderListSerializer
    }

    queryset = Order.objects.all()
