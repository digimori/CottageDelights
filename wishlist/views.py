from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def wishlist(request):
    """ A view to return the index page """

    return render(request, 'wishlist/wishlist.html')