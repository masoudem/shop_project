from django.urls import path
from .views import PanelView

urlpatterns = [
    path('panel/', PanelView.as_view(), name='panel'),
]