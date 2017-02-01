from rest_framework import serializers

from core.models import Order
from .common import OrderItemInlineSerializer

__all__ = ['OrderListSerializer']


class OrderListSerializer(serializers.ModelSerializer):
    items = OrderItemInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('external_id', 'status', 'items')

