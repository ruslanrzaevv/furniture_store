from django.shortcuts import render, redirect, get_object_or_404

from goods.models import Products
from carts.models import Cart

def cart_add(request, product_slug):
    print('hellooooooo')
    product = Products.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            print("Creating a new cart item")
            Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect('index ')


def cart_change(request):
    ...


def cart_remove(request, product_slug):
    return render(request, 'carts/cart_remove.html')