from django.shortcuts import render
from catalog.models import Product

def home(request):
    products = Product.objects.filter(is_available=True)[:6]
    return render(request, 'core/home.html', {
        'products': products
    })
