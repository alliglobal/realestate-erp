from django.contrib import admin
from .models import Project, Product

# Đăng ký Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


# Đăng ký Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'project', 'price', 'area', 'status']
    list_filter = ['status', 'project']
    search_fields = ['code', 'project__name']
    ordering = ['code']