from django.urls import path

from admins.views import index, UserListView, UserUpdateView, UserCreateView, UserDeleteView, \
    CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('categories/', CategoryListView.as_view(), name='admin_categories'),
    path('categories/create/', CategoryCreateView.as_view(), name='admin_categories_create'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='admin_categories_update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='admin_categories_delete'),
]
