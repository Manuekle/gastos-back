from django.urls import path
from base.views import revenues_views as views

urlpatterns = [
    path('<str:pk>/', views.getRevenue, name="revenue"),
]
