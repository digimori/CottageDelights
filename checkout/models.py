import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class OrderRecord(models.Model):
    order_number = models.CharField(max_length=50, null=False, editable=False)
    full_name = models.CharField(max_length=65, null=False, blank=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    home_number = models.CharField(max_length=20, null=False, blank=False)
    house_name = models.CharField(max_length=30, null=True, blank=True)
    address_line_1 = models.CharField(max_length=80, null=False, blank=False)
    address_line_2 = models.CharField(max_length=80, null=True, blank=True)
    town_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    shopping_cart = models.TextField(null=False, blank=False, default='')
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True)
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _create_order_number(self):
        """
        This function will generate a random
        and unique order number using the imported UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Each time a new line item is added,
        the grand total will update whilst also accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        OrderRecord, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        This will override the original save method
        to set the line item total and to then update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
