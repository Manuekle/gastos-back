from rest_framework import serializers

from .models import Revenue

"""
    Serializador de ingresos
    - Meta: se define el modelo y los campos que se van a serializar
"""

class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'
        
        