from django.apps import AppConfig

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        # Chỉ import signals khi app đã sẵn sàng hoàn toàn
        try:
            import products.signals
        except ImportError:
            pass  # Tránh lỗi khi chạy migrate hoặc tests