from django.urls import path
from .views import ProductView, OrderView
 
urlpatterns = [
    path('product/order', OrderView.as_view(), name='order-items'),
    path('product/<str:sku>', ProductView.as_view(), name='get-single-items'),
    path('product', ProductView.as_view(), name='get-all-items'),
    path('inventories/product/<str:sku>', ProductView.as_view(), name='update-item-stock'),
    
]