from rest_framework import serializers
from core.models import Order, OrderItem

class OrderItemRetrieveSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(read_only=True, slug_field='external_id')

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'price')
