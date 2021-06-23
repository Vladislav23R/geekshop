from django.shortcuts import render
from django.views.generic import ListView


from products.models import Product, ProductCategory
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


# def products(request, category_id=None, page=1):
#     context = {'title': 'Products', 'categories': ProductCategory.objects.all()}
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#
#     paginator = Paginator(products, 3)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#     context['products'] = products_paginator
#     return render(request, 'products/products.html', context)

# ToDo доделать фильтрацию по категория
class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Товары'
        context['categories'] = ProductCategory.objects.all()
        return context


