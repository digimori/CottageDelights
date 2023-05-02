from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    sender : Signal sent by: OrderLineItem class
    instance: Instance of the model that sent the signal
    created: Boolean sent by Django referring to whether this is a new instance
    or being updated.
    kwargs: Keyword arguments
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    instance.order.update_total()
