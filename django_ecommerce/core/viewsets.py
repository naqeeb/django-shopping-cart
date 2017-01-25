from rest_framework import viewsets

from core.rest.viewsets import BaseViewSet

from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(BaseViewSet, viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
