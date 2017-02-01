from rest_framework import serializers

from core.models import Order, OrderItem
from .common import OrderItemInlineSerializer

__all__ = ['OrderRetrieveSerializer']


class OrderRetrieveSerializer(serializers.ModelSerializer):
    items = OrderItemInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('external_id', 'status', 'items', 'total')

