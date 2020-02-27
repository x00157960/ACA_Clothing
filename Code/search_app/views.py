from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def dearch_results(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contins=query) | Q(description__contains=query))
    retuen render(request, 'search.html', {'query':query, 'products':products})
    