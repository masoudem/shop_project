from django.urls import path

from .views import SignUpView, sign_in
from .api_views import SignUpApi
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', sign_in, name='signin'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', SignUpApi.as_view(), name='api_signup'),
]