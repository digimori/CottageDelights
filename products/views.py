from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)


def productdetails(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/productdetails.html', context)
