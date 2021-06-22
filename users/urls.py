from django.urls import path

from users.views import UserLoginView, UserRegisterView, logout, profile

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]
