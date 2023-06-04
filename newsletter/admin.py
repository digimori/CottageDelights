from django.contrib import admin
from .models import Newsletter, MailMessage

# Register your models here.


admin.site.register(Newsletter)
admin.site.register(MailMessage)