from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Newsletter, MailMessage
from .forms import NewsletterForm

# Create your views here.


def Newsletter(request):
    form = NewsletterForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/newsletter.html', context)


def MailMessage(request):
    context = {

    }
    return render(request, 'newsletter/mailmessage.html', context)
