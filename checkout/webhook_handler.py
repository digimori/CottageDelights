from django.http import HttpResponse

from .models import OrderRecord, OrderLineItem
from products.models import Product

import json
import time


class StripeHandler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

# Handles payment success

    def handle_payment_success(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = OrderRecord.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    mobile_number__iexact=shipping_details.mobile_phone,
                    home_number__iexact=shipping_details.home_phone,
                    house_name__iexact=shipping_details.house_name,
                    address_line_1__iexact=shipping_details.address.line1,
                    address_line_2__iexact=shipping_details.address.line2,
                    town_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.county,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    shopping_cart=cart,
                    grand_total=grand_total,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Order Verified',
                status=200)
        else:
            order = None
            try:
                order = OrderRecord.objects.create(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    mobile_number__iexact=shipping_details.mobile_phone,
                    home_number__iexact=shipping_details.home_phone,
                    house_name__iexact=shipping_details.house_name,
                    address_line_1__iexact=shipping_details.address.line1,
                    address_line_2__iexact=shipping_details.address.line2,
                    town_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.county,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    shopping_cart=cart,
                    grand_total=grand_total,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

# Handles payment failure

    def handle_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)