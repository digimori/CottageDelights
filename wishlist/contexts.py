from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def wishlist_contents(request):

    wishlist_items = []
    product_quant = 0
    wishlist = request.session.get('wishlist', {})

    for item_id, item_data in wishlist.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            product_quant += item_data
            wishlist_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)

    context = {
        'wishlist_items': wishlist_items,
        'product_quant': product_quant,
    }

    return context
