from django.shortcuts import render
from django.contrib import messages
from .models import ContactForm


def Contact_Form(request):
    """ Contact Form Submission """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        order_number = request.POST.get('order_number')
        description = request.POST.get('description')

        query = ContactForm(
            name=name, email=email,
            order_number=order_number, description=description)
        query.save()
        messages.info(
            request,
            "Thanks for your message, we will respond soon!")

    return render(request, 'contactform/contact.html')
