from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import OrderRecord, OrderLineItem
from products.models import Product
from cart.contexts import cart_contents

import json


def checkout(request):
    """ A view to return the checkout page """

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'mobile_number': request.POST['mobile_number'],
            'home_number': request.POST['home_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_city': request.POST['town_city'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'county': request.POST['county'],
        }
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.stripe_pid = pid
            order.shopping_cart = json.dumps(cart)
            order.save()

        current_cart = cart_contents(request)
        total = current_cart['grand_total']

    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)
