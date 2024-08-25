from django.shortcuts import render, redirect

from goods.models import Products
from carts.models import Cart


def cart_add(request, slug):
    print('helloooooo')
    product = Products.objects.get(slug=slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request):
    ...


def cart_remove(request, product_slug): 
    return render(request, 'carts/cart_remove.html')








