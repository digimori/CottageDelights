from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def wishlist(request):
    """ A view to return the index page """

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        wishlist[item_id] += quantity
    else:
        wishlist[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['wishlist'] = wishlist

    return redirect(redirect_url)
