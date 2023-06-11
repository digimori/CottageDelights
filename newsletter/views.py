from django.shortcuts import render, HttpResponse, redirect, reverse
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

    form = MailMessageForm()

    if request.method == "POST":
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            from_email = settings.EMAIL_HOST_USER
            connection = mail.get_connection()
            connection.open()
            email_message = mail.EmailMessage(
                f'Email from {name}',
                f'Email: {email}\nOrder Number: {order_number}',
                f'QUERY : {description}',
                from_email, [os.environ.EMAIL_HOST],
                connection=connection)
            connection.send_messages([email_message])
            connection.close()
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