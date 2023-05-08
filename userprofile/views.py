from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.
def userprofile(request):
    """ View to return a profile page """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'userprofile/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
