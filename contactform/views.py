from django.shortcuts import render


def ContactForm(request):
    """ A view to return the contact page """

    return render(request, 'contactform/contact.html')
