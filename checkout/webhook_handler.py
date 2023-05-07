from django.http import HttpResponse

# Used to handle webhooks


class StripeHandler:
    def __init__(self):
        self.request = request

# Handle generic/unknown/unexpected webhook events

    def handle_event(self, event):
        return HttpResponse(
            content=f'webhook received:{event["type"]}',
            status=200
        )
# Handles payment intent success webhook event

    def handle_payment_success(self, event):
        return HttpResponse(
            content=f'webhook received:{event["type"]}',
            status=200
        )
# Handles Payment intent failure

    def handle_payment_failure(self, event):
        return HttpResponse(
            content=f'webhook received:{event["type"]}',
            status=200
        )
