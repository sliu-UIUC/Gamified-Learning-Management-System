from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .userInventory import UserInventory
from .forms import InventoryAddProductForm

@require_POST
def inventory_add(request, product_id):
    inventory = UserInventory(request)
    product = get_object_or_404(Product, id=product_id)
    form = InventoryAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        inventory.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('userInventory:inventory_detail')

def inventory_remove(request, product_id):
    inventory = UserInventory(request)
    product = get_object_or_404(Product, id=product_id)
    inventory.remove(product)
    return redirect('userInventory:inventory_detail')

def inventory_detail(request):
    inventory = UserInventory(request)
    return render(request, 'userInventory/detail.html', {'userInventory': inventory})