from django.urls import path, re_path
from .views import BasketListView, CreateCategory, CreateProduct, CreateShop, CreateTag, DeleteShop, PanelView, ProductListView, ShopDetailView, ShopListView, UpdateShop, BasketDetailView

urlpatterns = [
    path('panel/', PanelView.as_view(), name='panel'),
    path('create_shop/', CreateShop.as_view(), name='create_shop'),
    path('create_product/<int:pk>', CreateProduct.as_view(), name='create_product'),
    path('create_category/', CreateCategory.as_view(), name='create_category'),
    path('create_tag/', CreateTag.as_view(), name='create_tag'),
    path('shop_list/', ShopListView.as_view(), name='shop-list'),
    path('Product_list/<int:pk>', ProductListView.as_view(), name='product-list'),
    path('‍basket_list/<str:name>/', BasketListView.as_view(), name='basket-list'),
    path('shop_detail/<int:pk>', ShopDetailView.as_view(), name='shop-detail'),
    path('basket_detail/<int:pk>', BasketDetailView.as_view(), name='basket-detail'),
    path('update_shop/<int:pk>', UpdateShop.as_view(), name='update_shop'),
    path('delete_shop/<int:pk>', DeleteShop.as_view(), name='delete_shop'),
]
