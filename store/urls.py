from django.urls import path
from .views import StoreCreateView, StoreItemCreateView

urlpatterns = [
    path('store/create/', StoreCreateView.as_view(), name='store-create'),
    path('store-item/create/', StoreItemCreateView.as_view(), name='store-item-create'),
]