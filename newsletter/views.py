from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Newsletter, MailMessage

# Create your views here.


def Newsletter(request):
    context = {

    }
    return render(request, 'newsletter/newsletter.html', context)


def MailMessage(request):
    context = {

    }
    return render(request, 'newsletter/mailmessage.html', context)
