# authentication/urls/auth_urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from ..views.auth_views import UserRegisterView, LogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('logout/', LogoutView.as_view(), name='user_logout'),                
]