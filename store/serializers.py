from rest_framework import serializers
from .models import Store, StoreItem

class StoreItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreItem
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    items = StoreItemSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = '__all__'
