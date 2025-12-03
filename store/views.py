from django.shortcuts import render
from .models import Product

def store_list(request):
    products = Product.objects.filter(available=True)
    context = {'products': products}
    return render(request, 'store/store_list.html', context)