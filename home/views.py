from django.shortcuts import render, HttpResponse


def tester(request):
    return HttpResponse("Hello, This is a test")
