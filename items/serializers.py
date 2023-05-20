from django.shortcuts import get_object_or_404
from rest_framework import serializers

from stores.models import Store
from .models import Item
class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ['id','name', 'description','cost','price','quantity']
    def validate(self, attrs):
        store_id = self.context['view'].kwargs.get('store_id')
        store = get_object_or_404(Store, id=store_id)
        if store.owner != self.context['request'].user:
            raise serializers.ValidationError('Invalid user')
        return attrs    