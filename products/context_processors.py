from baskets.models import Baskets


def basket(request):
    basket_list = []
    if request.user.is_authenticated:
        basket_list = Baskets.objects.filter(user=request.user)

    return {
        'basket': basket_list,
    }