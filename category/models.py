from django.db import models

# Create your models here.


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
    
    name = models.CharField(
        max_length=200, choices=categories, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name
