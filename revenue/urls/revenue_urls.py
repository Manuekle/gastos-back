from django.urls import path
from revenue.views import revenue_views as views

"""
    Se crean las rutas de la aplicación de ingresos
"""

urlpatterns = [
    path('', views.getRevenues, name="revenues"),
    path('add/', views.addRevenue, name="revenue-add"),
    path('view/<str:pk>/', views.getRevenueById, name="revenue-id"),
    path('update/<str:pk>/', views.updateRevenue, name="revenue-update"),
    path('delete/<str:pk>/', views.deleteRevenue, name="revenue-delete"),
]
