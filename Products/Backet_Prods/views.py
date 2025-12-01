from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Product, Basket, BasketItem
from .forms import BasketForm


@login_required
def basket(request):
    basket = Basket.objects.get_or_create(user=request.user)
    return render(request, "basket.html", {"basket": basket})



@login_required
def basket_add(request, prod_id):
    basket = Basket.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=prod_id)
    
    form = BasketForm(request.POST or None)
    if form.is_valid():
        quantity = form.cleaned_data["quantity"]
        item = BasketItem.objects.get_or_create(basket=basket, product=product)
        if not item:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()
    return redirect("basket")


@login_required
def basket_del(request, prod_id):
    basket = Basket.objects.get_or_create(user=request.user)
    item = get_object_or_404(BasketItem, basket=basket, prod_id=prod_id)
    item.delete()
    return redirect("basket")


@login_required
def basket_clear(request):
    basket = Basket.objects.get_or_create(user=request.user)
    basket.items.all().delete()
    return redirect("basket")