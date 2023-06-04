from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    order_number = models.CharField(max_length=30)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'Message from {self.name}'
