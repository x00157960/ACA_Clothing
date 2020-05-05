import stripe
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render

def payment(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(12345)
    description = 'ACA  - New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'ship.html', dict(data_key = data_key, stripe_total = stripe_total, description = description))