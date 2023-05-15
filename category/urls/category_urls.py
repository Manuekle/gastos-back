from django.urls import path
from .. import views

urlpatterns = [
    path('', views.getCategory, name="category"),
    path('add/', views.addCategory, name="category-add"),
    path('update/<str:pk>/', views.updateCategory, name="category-update"),
    path('delete/<str:pk>/', views.deleteCategory, name="category-delete"),
]
