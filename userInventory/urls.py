from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'userInventory'

urlpatterns = [
    path('', views.inventory_detail, name='inventory_detail'),
    path('add/(?P<product_id>\d+)',
        views.inventory_add,
        name='inventory_add'),
    path('remove/(?P<product_id>\d+)',
        views.inventory_remove,
        name='inventory_remove'),
]