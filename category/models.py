from django.db import models
from django.contrib.auth.models import User

"""
    Modelo de categorias
    - user: usuario que ha creado la categoria
    - name: nombre de la categoria
    - price: precio de la categoria
    - createdAt: fecha de creación
    - id: id de la categoria
"""

class Categories(models.Model):

    categories = (
        ('servicio publicos', 'Servicio Publicos'),
        ('alimentos', 'Alimentos'),
        ('ropa', 'Ropa'),
        ('salud', 'Salud'),
        ('educacion', 'Educacion'),
        ('tecnologia', 'Tecnologia'),
        ('transporte', 'Transporte'),
        ('vivienda', 'Vivienda'),
        ('otros', 'Otros'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(
        max_length=200, choices=categories, blank=True)
    price = models.DecimalField(
        max_digits=12, decimal_places=0, default=0, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

"""
    cuando se agrege el monto de categoria se debe restar del monto total de ingresos
    ejemplo:

    Tiene 10000 en ingresos y 5000 en categoria de servicios publicos
    el monto total de ingresos debe ser 5000       
"""
