from django.urls import path

from products.views import index, ProductListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('<int:category_id>/', ProductListView.as_view(), name='product'),
    path('page/<int:page>/', ProductListView.as_view(), name='page'),
]
