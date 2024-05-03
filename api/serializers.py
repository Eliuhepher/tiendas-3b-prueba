from django.db.models import fields
from rest_framework import serializers
from .models import Product, Order
 
class ProductPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('sku', 'stock') 


class ProductPatchRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('stock',) 


class ProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('sku', 'name', 'stock') 


class ProductResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('sku', 'name', 'stock')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'