from unicodedata import name
from django.urls import path, re_path
from .views import BasketListView, CreateCategory, CreateProduct, CreateShop, CreateTag, DeleteShop, PanelView, ProductListView, ShopDetailView, ShopListView, UpdateShop, BasketDetailView, ChartView
from .api_views import BasketActive, BasketVerify, BasketVerifyView, CartItemAddView, CartItemDelView, CartItemView, ProductAPIList, ShopAPIList, CartItemAddOneView, CartItemReduceOneView


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
    path('chart/<int:pk>', ChartView.as_view(), name='chart'),
    #api
    path('api/shop_list/', ShopAPIList.as_view(), name = 'shop_api_list' ),
    path('api/shop_list/<int:pk>', ProductAPIList.as_view(), name = 'product_api_list' ),
    path('api/basket_act/', BasketActive.as_view(), name = 'active' ),
    path('api/basket_vrf/', BasketVerify.as_view(), name = 'verify' ),
    path('api/cart_item/', CartItemView.as_view(), name = 'cart_item' ),
    path('api/cart_add/', CartItemAddView.as_view(), name = 'cart_add' ),
    path('api/cart_del/<int:pk>', CartItemDelView.as_view(), name = 'cart_del' ),
    path('api/add_one/<int:pk>/', CartItemAddOneView.as_view(), name='add_cart'),
    path('api/reduce_one/<int:pk>/', CartItemReduceOneView.as_view(), name='reduce_cart'),
    path('api/verify/<int:pk>/', BasketVerifyView.as_view(), name='verify'),
    
]
