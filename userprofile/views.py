from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.
def userprofile(request):
    """ View to return a profile page """

    template = 'userprofile/profile.html'
    context = {
    }

    return render(request, template, context)
