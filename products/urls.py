from django.urls import path
from .views import product_list, change_status

urlpatterns = [
    path('', product_list, name='product_list'),
    path('change/<int:pk>/', change_status, name='change_status'),
]