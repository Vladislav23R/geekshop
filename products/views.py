from django.shortcuts import render

from products.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request):

    goods = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'title': 'Products',
        'products': goods,
        'categories': categories,
    }
    return render(request, 'products/products.html', context)
