from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.select_related('project').all()
    return render(request, 'product_list.html', {'products': products})


def change_status(request, pk):
    """Đổi trạng thái sản phẩm"""
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['available', 'reserved', 'sold']:
            product.status = new_status
            product.save()
            return redirect('product_list')
    
    return render(request, 'change_status.html', {'product': product})