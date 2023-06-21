from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import OrderRecord, OrderLineItem
from products.models import Product
from userprofile.models import UserProfile


import json
import time
import stripe


class StripeHandler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

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

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        billing_details = stripe_charge.billing_details  # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile data for save_info
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(
                user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone_number
                profile.default_house_name = shipping_details.house_name
                profile.default_address_line_1 = shipping_details.address.line1
                profile.default_address_line_2 = shipping_details.address.line2
                profile.default_town_city = shipping_details.address.city
                profile.default_county = shipping_details.address.county
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = OrderRecord.objects.get(
                    full_name__iexact=shipping_details.name,
                    userprofile=profile,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone_number,
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
            except OrderRecord.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                         'Verified order already in database'),
                status=200)
        else:
            order = None
            try:
                order = OrderRecord.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone_number,
                    house_name=shipping_details.house_name,
                    address_line_1=shipping_details.address.line1,
                    address_line_2=shipping_details.address.line2,
                    town_city=shipping_details.address.city,
                    county=shipping_details.address.county,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
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
        self._send_confirmation_email(order)
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
