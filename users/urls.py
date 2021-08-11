from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import UserLoginView, register, UserLogoutView, UserProfileView, verify, UserRegisterView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('verify/<email>/<activation_key>/', verify, name='verify'),
]
