from django.shortcuts import render, request


def index(request):
    """
    A view to return the index page
    """
    return render(request, 'home/index.html')
