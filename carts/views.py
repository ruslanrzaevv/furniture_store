from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from goods.models import Products
from carts.models import Cart


def cart_add(request, prod_slug):
    product = Products.objects.get(slug=prod_slug)
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, product=product)
        if cart.exists():
            cart = cart.first()
            if cart:
                cart.quantity += 1
                cart.save()
    else:
        Cart.objects.create(user=request.user, product=product,quantity=1)  
    redirect_url = request.META.get('HTTP_REFERER', '/')
    return redirect(redirect_url)


def cart_change(request):
    ...


def cart_remove(request, cart_id): 
    cart = get_object_or_404(Cart, id=cart_id)
    cart.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


















