from .views import *
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings


urlpatterns = [
	path('posts/', PostList.as_view(), name='posts'),
	path('post_detail/<slug:slug>/', post_detail, name='post_detail'),
	path('search/', search, name='search_list'),
	path('all_category/', CategoryList.as_view(), name='all_category'),
	path('category_detail/<int:id>/', category_detail, name='category_detail'),
	path('tag_list/', TagList.as_view(), name='tag_list'),
	path('tag_detail/<int:id>/', tag_detail, name='tag_detail'),
	path('update_post/<slug:slug>/', update_post, name='update_post'),
	path('delete_post/<slug:slug>/', delete_post, name='delete_post'),
	path('update_category/<int:id>/', update_category, name='update_category'),
	path('delete_category/<int:id>/', delete_category, name='delete_category'),
	path('create_category/', create_category, name='create_category'),
	path('update_tag/<int:id>/', update_tag, name='update_tag'),
	path('delete_tag/<int:id>/', delete_tag, name='delete_tag'),
	path('create_tag/', create_tag, name='create_tag'),
	path('create_post/', create_post, name='create_post'),
	path('login/', mylogin ,name="login"),
	path('register/', myRegister ,name="register"),
	path('dashboard/', dashboard ,name="dashboard"),
	path('avatar/', user_avatar ,name="avatar"),
	path("logout/", LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"),
]
