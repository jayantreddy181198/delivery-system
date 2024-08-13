from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FoodItemSerializer, BarItemSerializer, TotalCostSerializer
from .models import FoodItem, BarItem
from .utils import calculate_total_cost

class TotalCostView(APIView):
    def post(self, request):
        serializer = TotalCostSerializer(data=request.data)
        if serializer.is_valid():
            try:
                total_cost = calculate_total_cost(serializer.validated_data['items'])
                return Response({"total_cost": total_cost}, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodItemCreateView(APIView):
    def post(self, request):
        serializer = FoodItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            for item in serializer.validated_data:
                FoodItem.objects.using('postgres_db').create(**item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, category=None):
        if category:
            food_items = FoodItem.objects.using('postgres_db').filter(category=category)
        else:
            food_items = FoodItem.objects.using('postgres_db').all()
        serializer = FoodItemSerializer(food_items, many=True)
        return Response(serializer.data)

    def put(self, request):
        update_all = request.data.get('Update_All', False)
        update_data = request.data.get('data', [])
        updated_data = []
        if update_all:
            food_items = FoodItem.objects.using('postgres_db').all()
            for food_item in food_items:
                serializer = FoodItemSerializer(food_item, data=update_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    updated_data.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(updated_data)
        else:
            ids_to_update = [item['id'] for item in update_data]
            food_items = FoodItem.objects.using('postgres_db').filter(pk__in=ids_to_update)
            for food_item in food_items:
                for update in update_data:
                    if update['id'] == food_item.id:
                        serializer = FoodItemSerializer(food_item, data=update, partial=True)
                        if serializer.is_valid():
                            serializer.save()
                            updated_data.append(serializer.data)
                        else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(updated_data)

class BarItemCreateView(APIView):
    def post(self, request):
        serializer = BarItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            for item in serializer.validated_data:
                BarItem.objects.using('postgres_db').create(**item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, category=None):
        if category:
            bar_items = BarItem.objects.using('postgres_db').filter(category=category)
        else:
            bar_items = BarItem.objects.using('postgres_db').all()
        serializer = BarItemSerializer(bar_items, many=True)
        return Response(serializer.data)

    def put(self, request):
        update_all = request.data.get('Update_All', False)
        update_data = request.data.get('data', [])
        updated_data = []
        if update_all:
            bar_items = BarItem.objects.using('postgres_db').all()
            for bar_item in bar_items:
                serializer = BarItemSerializer(bar_item, data=update_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    updated_data.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(updated_data)
        else:
            ids_to_update = [item['id'] for item in update_data]
            bar_items = BarItem.objects.using('postgres_db').filter(pk__in=ids_to_update)
            for bar_item in bar_items:
                for update in update_data:
                    if update['id'] == bar_item.id:
                        serializer = BarItemSerializer(bar_item, data=update, partial=True)
                        if serializer.is_valid():
                            serializer.save()
                            updated_data.append(serializer.data)
                        else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(updated_data)
