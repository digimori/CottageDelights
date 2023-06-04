from django.db import models

# Create your models here.


class Newsletter(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    title = models.CharField(max_length=90, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title
