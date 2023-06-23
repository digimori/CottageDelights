from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Newsletter, MailMessage
from .forms import NewsletterForm, MailMessageForm
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage
from django.conf import settings

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
    if not request.user.is_superuser:
        messages.error(request, 'You must be an admin to access this page.')
        return redirect(reverse('home'))

    emails = Newsletter.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)

    if request.method == "POST":
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to subscribers!')
            return redirect('MailMessage')
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/mailmessage.html', context)
