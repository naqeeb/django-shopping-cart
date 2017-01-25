from rest_framework import serializers
from core.models import Order, OrderItem

__all__ = ['OrderListSerializer']

### Order Serializer ###
class OrderItemInlineSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(read_only=True, slug_field='external_id')

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'price')


class OrderListSerializer(serializers.ModelSerializer):
    items = OrderItemInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('external_id', 'status', 'items')

