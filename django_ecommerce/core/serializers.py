from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemInlineSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('external_id', 'status', 'items')

