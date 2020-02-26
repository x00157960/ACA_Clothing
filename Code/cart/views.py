import stripe
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Cart, CartItem
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

stripe.api_key = settings.STRIPE_SECRET_KEY

class CartPageView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='EUR',
            description='ACA Clothing',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')


def _cart_id(request):
	cart = request.session.session_key
	if not cart:
		cart = request.session.create()
	return cart


def add_cart(request, product_id):
	product = Product.objects.get(id=product_id)
	try:
		cart = Cart.objects.get(cart_id=_cart_id(request))
	except Cart.DoesNotExist:
		cart = Cart.objects.create(
				cart_id = _cart_id(request)
			)
		cart.save()
	try:
		cart_item = CartItem.objects.get(product=product, cart=cart)
		if cart_item.quantity < cart_item.product.stock:
			cart_item.quantity += 1
			cart_item.save()
		else:
			messages.add_message(request, messages.INFO, 
					'Sorry, no more of this item available')
	except CartItem.DoesNotExist:
		cart_item = CartItem.objects.create(
					product = product,
					quantity = 1,
					cart = cart
			)
		cart_item.save()
	return redirect('cart_detail')


def cart_detail(request, total=0, counter=0, cart_items = None):
	try:
		cart = Cart.objects.get(cart_id=_cart_id(request))
		cart_items = CartItem.objects.filter(cart=cart)
		for cart_item in cart_items:
			total += (cart_item.product.price * cart_item.quantity)
			counter += cart_item.quantity
	except ObjectDoesNotExist:
		pass
	return render(request, 'cart.html', dict(cart_items = cart_items, total = total, counter = counter))

def cart_remove(request, product_id):
	cart = Cart.objects.get(cart_id=_cart_id(request))
	product = get_object_or_404(Product, id=product_id)
	cart_item = CartItem.objects.get(product=product, cart=cart)
	if cart_item.quantity > 1:
		cart_item.quantity -= 1
		cart_item.save()
	else:
		cart_item.delete()
	return redirect('cart_detail')

def full_remove(request):
	cart = Cart.objects.get(cart_id=_cart_id(request))
	cart_items = CartItem.objects.filter(cart=cart)
	for cart_item in cart_items:
		cart_item.delete()
	return redirect('cart_detail')
