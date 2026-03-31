from django.contrib import admin
from django.urls import path, include
from dashboard.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),   # Đăng ký, login, logout
    path('', dashboard, name='dashboard'),
    path('products/', include('products.urls')),
]