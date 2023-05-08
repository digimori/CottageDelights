from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.
def userprofile(request):
    """ View to return a profile page """
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'userprofile/profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
