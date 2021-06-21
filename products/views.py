from django.shortcuts import render

from products.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {'title': 'Products', 'categories': ProductCategory.objects.all()}
    context.update({
        'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    })
    return render(request, 'products/products.html', context)
