from django.urls import path
from category.views import category_views as views

"""
    Se crean las rutas de la aplicación de categorias
"""

urlpatterns = [
    path('', views.getCategories, name="categories"),
    path('add/', views.addCategory, name="category-add"),
    path('view/<str:pk>/', views.getCategoryById, name="category-id"),
    path('update/<str:pk>/', views.updateCategory, name="category-update"),
    path('delete/<str:pk>/', views.deleteCategory, name="category-delete"),
]


