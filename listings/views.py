from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    categories=Category.objects.all()
    request_category=None
    products=Product.objects.all()

    if category_slug:
        request_category=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=request_category)

    return render(
        request,
        'product/list.html',
        {
            'categories':categories,
            'products':products
        }
    )
