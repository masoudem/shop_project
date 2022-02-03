from django.urls import path

from .views import SignUpView, sign_in
from .api_views import SignUpApi, UserList, OTPView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', sign_in, name='signin'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', SignUpApi.as_view(), name='api_signup'),
    path('profile/', UserList.as_view(), name='profile'),
    path('otp/', OTPView.as_view(), name='otp_view'),
]