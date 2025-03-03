from rest_framework import generics, permissions
from .models import Store
from .serializers import StoreSerializer, StoreItemSerializer
from rest_framework import serializers

class StoreCreateView(generics.CreateAPIView):
    """Allow vendors to create stores"""
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)

class StoreItemCreateView(generics.CreateAPIView):
    serializer_class = StoreItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        store_id = self.request.data.get('store')
        try:
            store = Store.objects.get(id=store_id, vendor=self.request.user)
            serializer.save(store=store)
        except Store.DoesNotExist:
            raise serializers.ValidationError("Invalid store ID or permission denied.")