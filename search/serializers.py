from rest_framework import serializers
from store.models import Store, StoreItem

class StoreSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'description', 'category', 'logo']

class StoreItemSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreItem
        fields = ['id', 'name', 'description', 'price', 'image']
