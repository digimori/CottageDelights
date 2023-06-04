from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Newsletter, MailMessage
from .forms import NewsletterForm, MailMessageForm
from django.core.mail import send_mail

# Create your views here.


def Newsletter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(
                request,
                "Thank you for Subscribing!")
            return redirect('/newsletter')
    else:
        form = NewsletterForm()

    context = {
        'form': form,
    }
    return render(request, 'newsletter/newsletter.html', context)


def MailMessage(request):
    form = MailMessageForm()
    if request.method == "POST":
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(
                request,
                "Message has been sent to subscribers!")
            return redirect('/newsletter/mailmessage')
    else:
        form = MailMessageForm()

    context = {
        'form': form,
    }
    return render(request, 'newsletter/mailmessage.html', context)
