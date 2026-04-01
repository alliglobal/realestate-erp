from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tên dự án")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS_CHOICES = [
        ('available', '🟢 Trống'),
        ('reserved', '🟡 Cọc'),
        ('sold', '🔴 Đã bán'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, unique=True, verbose_name="Mã căn/lô")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    price = models.DecimalField(max_digits=18, decimal_places=2)
    area = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        verbose_name = "Sản phẩm"

    def __str__(self):
        return f"{self.code} - {self.get_status_display()}"