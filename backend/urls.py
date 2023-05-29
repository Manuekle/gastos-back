""" backend URL Configuration

Se crean las ruta de las aplicaciones que se van a utilizar en
el proyecto y se incluyen en el archivo de rutas principal del proyecto.

"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls.user_urls')),
    path('category/', include('category.urls.category_urls')),
    path('revenue/', include('revenue.urls.revenue_urls')),
]
