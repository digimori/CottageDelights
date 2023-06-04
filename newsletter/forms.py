from django import forms
from .models import Newsletter, MailMessage


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email',]
