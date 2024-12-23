from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<str:pk>/', views.get_product),
]
