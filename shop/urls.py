from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('(?P<category_slug>[-\w]+)',
        views.product_list,
        name='product_list_by_category'),
    path('(?P<id>\d+)/(?P<slug>[-\w]+)',
        views.product_detail,
        name='product_detail'),
]