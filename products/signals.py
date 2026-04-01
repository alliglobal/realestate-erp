from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def broadcast_product_status(sender, instance, **kwargs):
    """Broadcast thay đổi trạng thái sản phẩm qua WebSocket"""
    try:
        from channels.layers import get_channel_layer
        from asgiref.sync import async_to_sync
        
        channel_layer = get_channel_layer()
        if channel_layer:
            async_to_sync(channel_layer.group_send)(
                "product_updates",
                {
                    "type": "product.update",
                    "product_id": instance.id,
                    "code": instance.code,
                    "status": instance.status,
                    "status_display": instance.get_status_display(),
                }
            )
    except Exception:
        # Nếu Channels chưa sẵn sàng (ví dụ: chạy migrate), bỏ qua
        pass