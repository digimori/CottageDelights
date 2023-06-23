from django import forms
from .models import Newsletter, MailMessage


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email', ]


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        # The below is getting all of the class keys from the MailMessage class
        fields = '__all__'
