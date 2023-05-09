from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.forms import OrderForm
from checkout.models import OrderRecord, OrderLineItem


# Create your views here.
def userprofile(request):
    """ View to return a profile page """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            # Toast message here

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'userprofile/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(OrderRecord, order_number=order_number)

    # Toast message here confirming order numbers

    template = 'checkout/checkoutcomplete.html'
    context = {
        'order': order,
        'from_profile': True
    }
    return render(request, template, context)
