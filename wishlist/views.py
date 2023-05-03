from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def wishlist(request):
    """ A view to return the wishlist page """

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url_wish = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        wishlist[item_id] += quantity
    else:
        wishlist[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['wishlist'] = wishlist

    return redirect(redirect_url)


def adjust_wishlist(request, item_id):
    quantity = int(request.POST.get('quantity'))
    wishlist = request.session.get('wishlist', {})

    if quantity > 0:
        wishlist[item_id] = quantity
    else:
        wishlist.pop[item_id]

    request.session['wishlist'] = wishlist
    return redirect(reverse('view_wishlist'))


def remove_from_wishlist(request, item_id):
    """Remove the item from wishlist"""

    product = Product.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    wishlist.pop(item_id)
    messages.success(request, f'Removed {product.name} from your wishlist')

    return redirect(reverse('view_wishlist'))
