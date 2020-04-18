from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .userInventory import UserInventory
from .forms import InventoryAddProductForm
from django.contrib.auth.models import User


@require_POST
def inventory_add(request, product_id):
    if request.user.is_authenticated:
        inventory = UserInventory(request)
        product = get_object_or_404(Product, id=product_id)
        form = InventoryAddProductForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            cur_user = request.user
            cur_money = cur_user.profile.money 
            total_price = cd['quantity']*product.price
            if(total_price<=cur_money): 
                cur_user.profile.money -=total_price
                cur_user.save()
                inventory.add(product=product, quantity=cd['quantity'],update_quantity=cd['update'])
        return redirect('userInventory:inventory_detail')
    return redirect('login')

def inventory_remove(request, product_id):
    inventory = UserInventory(request)
    product = get_object_or_404(Product, id=product_id)
    inventory.remove(product)
    return redirect('userInventory:inventory_detail')

def inventory_detail(request):
    inventory = UserInventory(request)
    return render(request, 'userInventory/detail.html', {'userInventory': inventory})