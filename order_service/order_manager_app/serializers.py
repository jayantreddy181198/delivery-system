from rest_framework import serializers
from .models import OrderItems

class OrderItemsSerializer(serializers.ModelSerializer):
    items = serializers.JSONField()
    
    class Meta:
        model = OrderItems
        fields = '__all__'
