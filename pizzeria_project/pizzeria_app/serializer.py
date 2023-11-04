# In pizzeria_app/serializers.py

from rest_framework import serializers
from .models import Pizza, Order

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
