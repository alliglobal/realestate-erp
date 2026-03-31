from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import Group

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=150, label="Họ và tên", required=True)
    role = forms.ChoiceField(
        choices=[
            ('Sale', 'Nhân viên Sale'),
            ('Manager', 'Quản lý')
        ],
        label="Vai trò",
        required=True,
        widget=forms.Select(attrs={'class': 'w-full px-4 py-3 border rounded-xl'})
    )

    def save(self, request):
        # Gọi save gốc của allauth để tạo user
        user = super().save(request)
        
        # Lưu thêm họ tên
        user.first_name = self.cleaned_data.get('first_name', '')
        user.save()

        # Gán nhóm quyền theo vai trò
        role = self.cleaned_data.get('role')
        try:
            if role == 'Sale':
                group = Group.objects.get(name='Sale')
            else:
                group = Group.objects.get(name='Manager')
            user.groups.add(group)
        except Group.DoesNotExist:
            pass  # Nếu chưa tạo group thì bỏ qua

        return user