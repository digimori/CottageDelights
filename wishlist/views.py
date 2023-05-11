from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

from django.contrib.auth.decorators import login_required


@login_required
def wishlist(request):
    """ A view to return the wishlist page """

    return render(request, 'wishlist/wishlist.html')


@login_required
def add_to_wishlist(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url_wish = request.POST.get('redirect_url_wish')
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        wishlist[item_id] += quantity
        messages.success(request, f'Added {product.name} to your wishlist')

    request.session['wishlist'] = wishlist

    return redirect(redirect_url_wish)


@login_required
def adjust_wishlist(request, item_id):
    quantity = int(request.POST.get('quantity'))
    wishlist = request.session.get('wishlist', {})

    if quantity > 0:
        wishlist[item_id] = quantity
    else:
        wishlist.pop[item_id]

    request.session['wishlist'] = wishlist
    return redirect(reverse('view_wishlist'))


@login_required
def remove_from_wishlist(request, item_id):
    """Remove the item from wishlist"""

    product = Product.objects.get(pk=item_id)
    redirect_url_wish = request.POST.get('redirect_url_wish')
    wishlist = request.session.get('wishlist', {})

    wishlist.pop(item_id)
    messages.success(request, f'Removed {product.name} from your wishlist')

    return redirect(reverse('view_wishlist'))
