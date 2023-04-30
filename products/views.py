from django.shortcuts import render, get_object_or_404, reverse
from .models import Product
from django.contrib import messages
from django.db.models import Q


def all_products(request):
    products = Product.objects.all()

    query = None
    if request.GET:
        if 'q' in request.GET['q']:
            if not query:
                messages.error(
                    request, 'Please enter valid search criteria')
                return redirect(reverse, 'products')

            queries = Q(
                name__, contains=query) | Q(description__, contains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query
    }
    return render(request, 'products/products.html', context)


def productdetails(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/productdetails.html', context)
