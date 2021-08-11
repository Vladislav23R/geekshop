from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import UserLoginView, register, UserLogoutView, UserProfileView, verify

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('verify/<email>/<activation_key>/', verify, name='verify'),
]
