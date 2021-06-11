from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from products.models import Product
from baskets.models import Baskets


@login_required()
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Baskets.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Baskets.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required()
def basket_remove(request, id):
    Baskets.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
