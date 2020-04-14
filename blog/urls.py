from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views
from shop import views as shop_view
from userInventory import views as inventory_view

urlpatterns = [
    path('', views.about, name='blog-about'),
    path('content/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
    #path('store/', views.shop, name='shop-page'),
    path('store/', shop_view.product_list, name='shop-page'), 
    path('inventory/', inventory_view.inventory_detail, name='inventory'), 
    path('plot1/', views.random_dialog, name='story1'),
]
