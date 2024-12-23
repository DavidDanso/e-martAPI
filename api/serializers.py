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