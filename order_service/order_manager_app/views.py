from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OrderItems
import json
from .serializers import OrderItemsSerializer
from menu_app.utils import calculate_total_cost  
from .tasks import publish_order_message

class OrderItemsView(APIView):
    def get(self, request, pk=None):
        if pk:
            order_item = OrderItems.objects.get(pk=pk)
            serializer = OrderItemsSerializer(order_item)
        else:
            order_items = OrderItems.objects.all()
            serializer = OrderItemsSerializer(order_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            # Calculate the total cost before saving the order
            total_cost = calculate_total_cost(request.data['items'])
            
            # Save the order with the calculated total cost
            order_data = request.data.copy()
            order_data['total'] = total_cost
            serializer = OrderItemsSerializer(data=order_data)
            
            if serializer.is_valid():
                serializer.save()
                order_item = {
                    'items': order_data['items'],
                    'total': float(order_data['total']),  # Convert Decimal to float
                    'email': order_data['email'],
                }
                publish_order_message.delay(json.dumps(order_item))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        order_item = OrderItems.objects.get(pk=pk)
        serializer = OrderItemsSerializer(order_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
