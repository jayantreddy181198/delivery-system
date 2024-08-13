from django.urls import path
from .views import OrderItemsView

urlpatterns = [
    path('api/create', OrderItemsView.as_view(), name='order-item-create'),
    path('api/get', OrderItemsView.as_view(), name='order-item-list'),
    path('api/get/<int:pk>', OrderItemsView.as_view(), name='order-item-list'),
    path('api/update/<int:pk>', OrderItemsView.as_view(), name='order-item-update'),
]