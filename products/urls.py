from django.urls import path

import products.views as products

app_name = products

urlpatterns = [
    path('', products, name='index')
]