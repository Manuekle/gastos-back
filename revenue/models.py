from django.db import models
from django.contrib.auth.models import User

"""
    Modelo de ingresos
    - user: usuario que ha creado el ingreso
    - name: nombre del ingreso
    - price: precio del ingreso
    - createdAt: fecha de creación
    - id: id del ingreso
"""

class Revenue(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(
        max_digits=12, decimal_places=0, default=0, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
    
    

 
