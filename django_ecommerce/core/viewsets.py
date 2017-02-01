from rest_framework import viewsets

from core.rest.viewsets import BaseViewSet

from .models import Order
from .serializers import OrderListSerializer, OrderRetrieveSerializer

class OrderViewSet(BaseViewSet, viewsets.ReadOnlyModelViewSet):
    serializers = {
        'list':    OrderListSerializer,
        'default':  OrderRetrieveSerializer
    }

    queryset = Order.objects.all()
