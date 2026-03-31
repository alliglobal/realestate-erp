from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Tạo các nhóm quyền Sale, Manager, Admin'

    def handle(self, *args, **options):
        # Tạo 3 nhóm
        admin_group, created = Group.objects.get_or_create(name='Admin')
        manager_group, _ = Group.objects.get_or_create(name='Manager')
        sale_group, _ = Group.objects.get_or_create(name='Sale')

        if created:
            # Admin có tất cả quyền
            admin_group.permissions.set(Permission.objects.all())

        self.stdout.write(self.style.SUCCESS('✅ Đã tạo xong 3 nhóm quyền: Admin, Manager, Sale'))
        self.stdout.write(self.style.SUCCESS('   - Admin: Toàn quyền'))
        self.stdout.write(self.style.SUCCESS('   - Manager: Quản lý team'))
        self.stdout.write(self.style.SUCCESS('   - Sale: Chỉ quản lý dữ liệu cá nhân'))
