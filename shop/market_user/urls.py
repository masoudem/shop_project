from django.urls import path
from .views import SignUpView, sign_in

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('signin/', SignInView.as_view(), name='signin'),
    path('signin/', sign_in, name='signin'),
]