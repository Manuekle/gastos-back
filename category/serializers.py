from rest_framework import serializers

from .models import Categories

"""
    Serializador de categorias
    - Meta: se define el modelo y los campos que se van a serializar
"""

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
