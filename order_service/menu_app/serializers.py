from rest_framework import serializers
from .models import FoodItem, BarItem

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'description', 'price', 'available', 'category']  # Include relevant fields

class BarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarItem
        fields = ['id', 'name', 'description', 'price', 'available', 'category', 'alcohol_content']  # Include relevant fields

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()

class TotalCostSerializer(serializers.Serializer):
    items = ItemSerializer(many=True)