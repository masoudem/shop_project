from django.urls import path
from .views import CreateShop, DeleteShop, PanelView, ShopDetailView, ShopListView, UpdateShop

urlpatterns = [
    path('panel/', PanelView.as_view(), name='panel'),
    path('create_shop/', CreateShop.as_view(), name='create_shop'),
    path('shop_list/', ShopListView.as_view(), name='shop-list'),
    path('shop_detail/<int:pk>', ShopDetailView.as_view(), name='shop-detail'),
    path('update_shop/<int:pk>', UpdateShop.as_view(), name='update_shop'),
    path('delete_shop/<int:pk>', DeleteShop.as_view(), name='delete_shop'),
]