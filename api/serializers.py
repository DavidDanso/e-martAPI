from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']

    def validate_price(self, value):
        if value <= 0:
            return serializers.ValidationError("Product price should be greater than 0.")
        return value



class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        source='product.price'
        )
    class Meta:
        model = OrderItem
        fields = ['product_name', 'product_price', 'quantity']



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total')

    def total(self, obj):
        order_items = obj.items.all()
        return sum(item.item_subtotal for item in order_items)
    class Meta:
        model = Order
        fields = ['order_id', 'user', 'status', 'items', 'total_price', 'created_at']