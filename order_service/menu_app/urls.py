from django.urls import path
from .views import FoodItemCreateView, BarItemCreateView, TotalCostView

urlpatterns = [
    path('api/food/create', FoodItemCreateView.as_view(), name='food-item-create'),
    path('api/food/getall', FoodItemCreateView.as_view(), name='food-item-list'),
    path('api/food/update', FoodItemCreateView.as_view(), name='food-item-update'),
    path('api/food/getall/<str:category>', FoodItemCreateView.as_view(), name='food-item-list'),
    path('api/bar/create', BarItemCreateView.as_view(), name='bar-item-create'),
    path('api/bar/getall', BarItemCreateView.as_view(), name='bar-item-list'),
    path('api/bar/getall/<str:category>', BarItemCreateView.as_view(), name='bar-item-list'),
    path('api/bar/update', BarItemCreateView.as_view(), name='bar-item-update'),
    path('api/total/cost', TotalCostView.as_view(), name='get-total-cost'),
]